import os
import re
import django
import pkg_resources
from sys import platform

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


class DjangoProjectStructurator(BaseStructurator):
    
    """Class to create Django Project with user choices and best folder structure.
    """
    
    def __init__(self) -> None:
        self.config = {}
    
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
        import keyword
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
        print("\n🌟 Next Steps for Your Django Project:")
        
        print("\n1. Create a Virtual Environment:")
        print(f"   cd {self.config['project_path']}")
        print("   python -m venv venv")
        
        print("\n2. Activate the Virtual Environment:")
        print("   venv\\Scripts\\activate")
        
        print("\n3. Install Project Dependencies:")
        print("   pip install -r .\\requirements\development.txt")
        
        print("\n4. Configure Database:")
        print("   Update DATABASE configuration & .env with your credentials")
        
        print("\n5. Run Database Migrations:")
        print("   cd src")
        print("   python manage.py migrate")
        
        print("\n6. Create Superuser (Optional):")
        print("   python manage.py createsuperuser")
        
        print("\n7. Run Development Server:")
        print("   python manage.py runserver")
    
    def _print_unix_success_help(self) -> None:
        """This function will print next steps for Linux/macOS user after creation of new Django Project.
        """
        print("\n🌟 Next Steps for Your Django Project:")
        
        print("\n1. Create a Virtual Environment:")
        print(f"   cd {self.config['project_path']}")
        print("   python3 -m venv venv")
        
        print("\n2. Activate the Virtual Environment:")
        print("   source venv/bin/activate")
        
        print("\n3. Install Project Dependencies:")
        print("   pip install -r ./requirements/development.txt")
        
        print("\n4. Configure Database:")
        print("   Update DATABASE configuration & .env with your credentials")
        
        print("\n5. Run Database Migrations:")
        print("   cd src")
        print("   python manage.py migrate")
        
        print("\n6. Create Superuser (Optional):")
        print("   python manage.py createsuperuser")
        
        print("\n7. Run Development Server:")
        print("   python manage.py runserver")
    
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
        self.config['django_structurator_version'] = pkg_resources.get_distribution("django_structurator").version
        
        self.config['secret_key'] = SECRET_KEY_INSECURE_PREFIX + get_random_secret_key()
        
        config = self.config
        
        print("\n🚀 Project Configuration Summary:")
        print("=" * 40)
        for key, value in config.items():
            print(f"{key}: {value}")
        print("=" * 40)
        
        print("")
        confirm = super()._yes_no_prompt("Do you want to proceed with project creation?", default=True)
        if confirm:
            
            if config.get("database") == 'sqlite':
                PROJECT_STRUCTURE['local_db'] = []
                
            if config.get("env") == 'no_env':
                PROJECT_STRUCTURE['src']['config'][None].remove('.env')
                PROJECT_STRUCTURE['src']['config'][None].remove('.env.example')
                
            if config.get("use_celery", False) == True:
                PROJECT_STRUCTURE['src']['config'][None].append("celery.py")
                
            folder_generator = FolderGenerator(
                self.config,
                PROJECT_STRUCTURE,
                PROJECT_TEMPLATE_DIR,
            )
            folder_generator.generate()
            
            print(f"Django project '{config['project_name']}' created successfully at {config['project_path']}")
            self.print_success_help()
        else:
            print("Project creation cancelled.")
        
        
def startproject():
    project_structurator = DjangoProjectStructurator()
    project_structurator.generate_project()
