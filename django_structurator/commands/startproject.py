import os
import re
import sys
import copy
import keyword
import django
from sys import platform
from importlib.metadata import version, PackageNotFoundError

from django.core.checks.security.base import SECRET_KEY_INSECURE_PREFIX
from django.core.management.utils import get_random_secret_key

from django_structurator.commands.base import BaseStructurator
from django_structurator.helpers.structures import PROJECT_STRUCTURE
from django_structurator.helpers.utils import FolderGenerator
from django_structurator.settings import (
    PROJECT_TEMPLATE_DIR,
    PROJECT_NAME_PATTERN,
    INVALID_PROJECT_NAME_MESSAGE,
    DISALLOWED_PROJECT_NAMES,
    DATABASE_CHOICES,
    DEFAULT_DATABASE,
    ENV_CHOICES,
    DEFAULT_ENV,
    DJANGO_PROJECT_FEATURES
)
from django_structurator.helpers.colors import Colors


class DjangoProjectStructurator(BaseStructurator):
    
    """Class to create Django Project with user choices and best folder structure.
    """
    
    def __init__(self, kwargs=None) -> None:
        self.config = {}
        self.kwargs = kwargs or {}
    
    def _project_name_validator(self, name: str) -> str:
        """Validator for Project Name.
        """
        if not name:
            raise ValueError("Project name cannot be empty.")

        if not re.match(PROJECT_NAME_PATTERN, name):
            raise ValueError(
                INVALID_PROJECT_NAME_MESSAGE
            )
        
        # Check against reserved keywords
        if name in keyword.kwlist:
            raise ValueError(f"Invalid project name. '{name}' is a reserved Python keyword.")
        
        # Check if the name matches common disallowed names
        if name.lower() in DISALLOWED_PROJECT_NAMES:
            raise ValueError(f"Invalid project name. '{name}' is disallowed.")
        
        return name
            
    def _path_validator(self, path: str) -> str:
        expanded_path = os.path.abspath(os.path.expanduser(path))
        
        # If path doesn't exist, ask to create
        if not os.path.exists(expanded_path):
            if self.kwargs and self.kwargs.get('no_que'):
                create = True
            else:
                create = super()._yes_no_prompt(
                    f"Path {expanded_path} does not exist. Do you want to create it?", 
                    default=True,
                )
            if create:
                try:
                    os.makedirs(expanded_path)
                except PermissionError:
                    raise ValueError(f"Permission denied: Cannot create directory {expanded_path}")
            else:
                raise ValueError("Path does not exist and was not created.")
        
        return expanded_path
    
    def _get_project_configurations(self) -> None:
        
        """This function will take all user choices and store it into class level config variable.
        """
        if self.kwargs and self.kwargs.get('no_que'):
            project_name = self.kwargs.get('name')
            if not project_name:
                print("Error: --name is required when using --no-que")
                sys.exit(1)
            self.config['project_name'] = self._project_name_validator(project_name)
            
            project_path = self.kwargs.get('path') or os.path.join(os.getcwd())
            self.config['project_path'] = self._path_validator(project_path)
            
            self.config['database'] = self.kwargs.get('db') or DEFAULT_DATABASE
            self.config['env'] = self.kwargs.get('env') or DEFAULT_ENV
            
            for feature, feature_key in DJANGO_PROJECT_FEATURES.items():
                self.config[feature_key] = self.kwargs.get(feature_key, False)
            return

        project_name = super()._prompt(
            "Enter project name",
            validator= self._project_name_validator
        )
        self.config['project_name'] = project_name
        
        default_path = os.path.join(os.getcwd())
        project_path = super()._prompt(
            "Enter project path", 
            default=default_path, 
            validator=self._path_validator
        )
        self.config['project_path'] = project_path
        
        database = super()._prompt(
            "Select database", 
            options = DATABASE_CHOICES,
            default= DEFAULT_DATABASE,
        )
        self.config['database'] = database
        
        env = super()._prompt(
            "Select ENV configuration", 
            options = ENV_CHOICES,
            default= DEFAULT_ENV,
        )
        self.config['env'] = env
        
        print("\n🔧 Optional Project Features:")
        for feature, feature_key in DJANGO_PROJECT_FEATURES.items():
            self.config[feature_key] = super()._yes_no_prompt(
                f"Do you want to use {feature}?", 
                default=False
            )
    
    def _print_windows_success_help(self) -> None:
        """This function will print next steps for Windows user after creation of new Django Project.
        """
        print(f"\n{Colors.OKGREEN}{Colors.BOLD}🌟 Next Steps for Your Django Project:{Colors.ENDC}")
        
        print(f"\n{Colors.OKCYAN}1. Create a Virtual Environment:{Colors.ENDC}")
        print(f"   {Colors.WARNING}cd {self.config['project_path']}{Colors.ENDC}")
        print(f"   {Colors.WARNING}python -m venv venv{Colors.ENDC}")
        
        print(f"\n{Colors.OKCYAN}2. Activate the Virtual Environment:{Colors.ENDC}")
        print(f"   {Colors.WARNING}venv\\Scripts\\activate{Colors.ENDC}")
        
        print(f"\n{Colors.OKCYAN}3. Install Project Dependencies:{Colors.ENDC}")
        print(f"   {Colors.WARNING}pip install -r .\\requirements\\development.txt{Colors.ENDC}")
        
        print(f"\n{Colors.OKCYAN}4. Configure Database:{Colors.ENDC}")
        print(f"   {Colors.WARNING}Update DATABASE configuration & .env with your credentials{Colors.ENDC}")
        
        print(f"\n{Colors.OKCYAN}5. Run Database Migrations:{Colors.ENDC}")
        print(f"   {Colors.WARNING}cd src{Colors.ENDC}")
        print(f"   {Colors.WARNING}python manage.py migrate{Colors.ENDC}")
        
        print(f"\n{Colors.OKCYAN}6. Create Superuser (Optional):{Colors.ENDC}")
        print(f"   {Colors.WARNING}python manage.py createsuperuser{Colors.ENDC}")
        
        print(f"\n{Colors.OKCYAN}7. Run Development Server:{Colors.ENDC}")
        print(f"   {Colors.WARNING}python manage.py runserver{Colors.ENDC}")
    
    def _print_unix_success_help(self) -> None:
        """This function will print next steps for Linux/macOS user after creation of new Django Project.
        """
        print(f"\n{Colors.OKGREEN}{Colors.BOLD}🌟 Next Steps for Your Django Project:{Colors.ENDC}")
        
        print(f"\n{Colors.OKCYAN}1. Create a Virtual Environment:{Colors.ENDC}")
        print(f"   {Colors.WARNING}cd {self.config['project_path']}{Colors.ENDC}")
        print(f"   {Colors.WARNING}python3 -m venv venv{Colors.ENDC}")
        
        print(f"\n{Colors.OKCYAN}2. Activate the Virtual Environment:{Colors.ENDC}")
        print(f"   {Colors.WARNING}source venv/bin/activate{Colors.ENDC}")
        
        print(f"\n{Colors.OKCYAN}3. Install Project Dependencies:{Colors.ENDC}")
        print(f"   {Colors.WARNING}pip install -r ./requirements/development.txt{Colors.ENDC}")
        
        print(f"\n{Colors.OKCYAN}4. Configure Database:{Colors.ENDC}")
        print(f"   {Colors.WARNING}Update DATABASE configuration & .env with your credentials{Colors.ENDC}")
        
        print(f"\n{Colors.OKCYAN}5. Run Database Migrations:{Colors.ENDC}")
        print(f"   {Colors.WARNING}cd src{Colors.ENDC}")
        print(f"   {Colors.WARNING}python manage.py migrate{Colors.ENDC}")
        
        print(f"\n{Colors.OKCYAN}6. Create Superuser (Optional):{Colors.ENDC}")
        print(f"   {Colors.WARNING}python manage.py createsuperuser{Colors.ENDC}")
        
        print(f"\n{Colors.OKCYAN}7. Run Development Server:{Colors.ENDC}")
        print(f"   {Colors.WARNING}python manage.py runserver{Colors.ENDC}")
    
    def print_success_help(self) -> None:
        """This function will call success_help function according to OS type.
        """
        if platform == "darwin" or platform == "linux" or platform == "linux2":
            self._print_unix_success_help()
        elif platform == "win32":
            self._print_windows_success_help()
        else:
            self._print_windows_success_help()
    
    def generate_project(self) -> None:
        
        """This function will use all above function to create Django project with user choices.
        """
        
        self._get_project_configurations()
        
        self.config['django_docs_version'] = django.get_version()
        try:
            self.config['django_structurator_version'] = version("django_structurator")
        except PackageNotFoundError:
            self.config['django_structurator_version'] = "unknown"
        
        self.config['secret_key'] = SECRET_KEY_INSECURE_PREFIX + get_random_secret_key()
        
        config = self.config
        
        print("\n🚀 Project Configuration Summary:")
        print("=" * 40)
        for key, value in config.items():
            print(f"{key}: {value}")
        print("=" * 40)
        
        print("")
        if self.kwargs and self.kwargs.get('no_que'):
            confirm = True
        else:
            confirm = super()._yes_no_prompt("Do you want to proceed with project creation?", default=True)
            
        if confirm:
            project_structure = copy.deepcopy(PROJECT_STRUCTURE)
            
            if config.get("database") == 'sqlite':
                project_structure['local_db'] = []
                
            if config.get("use_celery"):
                project_structure['src']['config'][None].append("celery.py")
                
            if config.get("use_logger"):
                project_structure['logs'] = []
                
            if config.get("use_docker"):
                project_structure[None].extend(['Dockerfile', 'docker-compose.yml', '.dockerignore'])
                project_structure['nginx'] = ['default.conf']
                
            folder_generator = FolderGenerator(
                self.config,
                project_structure,
                PROJECT_TEMPLATE_DIR,
            )
            folder_generator.generate()
            
            print(f"\n{Colors.OKGREEN}🎉 Django project '{config['project_name']}' created successfully at {config['project_path']}{Colors.ENDC}")
            self.print_success_help()
        else:
            print("Project creation cancelled.")
        
        
def startproject(kwargs=None):
    project_structurator = DjangoProjectStructurator(kwargs)
    project_structurator.generate_project()
