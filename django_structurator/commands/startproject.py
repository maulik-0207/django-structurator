import os
import re
import django
import pkg_resources
from sys import platform
from django.core.checks.security.base import SECRET_KEY_INSECURE_PREFIX
from django.core.management.utils import get_random_secret_key
from django_structurator.helpers.structures import PROJECT_STRUCTURE
from django_structurator.helpers.utils import FolderGenerator
from django_structurator.settings import (
    DISALLOWED_PROJECT_NAMES,
    PROJECT_NAME_PATTERN,
    DATABASE_CHOICES,
    DEFAULT_DATABASE,
    DJANGO_PROJECT_FEATURES,
    PROJECT_TEMPLATE_DIR
)


class DjangoProjectStructurator:
    
    def __init__(self):
        self.config = {}
        
    def _prompt(self, question, default = None, validator = None):
        while True:
            if default:
                prompt = f"{question} [{default}]: "
            else:
                prompt = f"{question}: "

            user_input = input(prompt).strip()
            
            if not user_input and default:
                return default
            
            if validator:
                try:
                    return validator(user_input)
                except ValueError as e:
                    print(f"{e}")
                    continue
            
            return user_input
        
    def _yes_no_prompt(self, question, default= False):
        default_str = 'Y/n' if default == True else 'y/N'
        
        while True:
            response = input(f"{question} [{default_str}]: ").lower().strip()
            
            if response in ['y', 'yes']:
                return True
            elif response in ['n', 'no']:
                return False
            elif response == '':
                return default
            else:
                print("Please respond with 'y' or 'n'.")
                
    def _path_validator(self, path):
        expanded_path = os.path.abspath(os.path.expanduser(path))
        
        # If path doesn't exist, ask to create
        if not os.path.exists(expanded_path):
            create = self._yes_no_prompt(
                f"Path {expanded_path} does not exist. Do you want to create it?", 
                default=True
            )
            if create:
                os.makedirs(expanded_path, exist_ok=True)
            else:
                raise ValueError("Path does not exist and was not created.")
        
        return expanded_path
    
    def _project_name_validator(self, name):
        if not name:
            raise ValueError("Project name cannot be empty.")

        if not re.match(PROJECT_NAME_PATTERN, name):
            raise ValueError(
                "It must start with a letter or an underscore, "
                "and contain only letters, numbers, and underscores."
            )
        
        # Check against reserved keywords
        import keyword
        if name in keyword.kwlist:
            raise ValueError(f"Invalid project name. '{name}' is a reserved Python keyword.")
        
        # Check if the name matches common disallowed names
        if name.lower() in DISALLOWED_PROJECT_NAMES:
            raise ValueError(f"Invalid project name. '{name}' is disallowed.")
        
        return name
    
    def _database_validator(self, database):
        if database in DATABASE_CHOICES:
            return database
        else:
            raise ValueError(f"Invalid database name({database})")
    
    def _get_project_configurations(self):
        project_name = self._prompt(
            "Enter project name", 
            validator= self._project_name_validator
        )
        self.config['project_name'] = project_name
        
        default_path = os.path.join(os.getcwd(), project_name)
        project_path = self._prompt(
            "Enter project path", 
            default=default_path, 
            validator=self._path_validator
        )
        self.config['project_path'] = project_path
        
        database = self._prompt(
            f"Select database ({', '.join(DATABASE_CHOICES)})", 
            default= DEFAULT_DATABASE,
            validator= self._database_validator
        )
        self.config['database'] = database
        
        print("\n🔧 Optional Project Features:")
        for feature, feature_key in DJANGO_PROJECT_FEATURES.items():
            self.config[feature_key] = self._yes_no_prompt(
                f"Do you want to use {feature}?", 
                default=False
            )
    
    def _print_windows_success_help(self):
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
    
    def _print_unix_success_help(self):
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
    
    def print_success_help(self):
        if platform == "darwin" or platform == "linux" or platform == "linux2":
            self._print_unix_success_help()
        elif platform == "win32":
            self._print_windows_success_help()
        else:
            self._print_windows_success_help()
    
    def generate_project(self):
        self._get_project_configurations()
        self.config['django_docs_version'] = django.get_version()
        self.config['django_structurator_version'] = pkg_resources.get_distribution("django_structurator").version
        self.config['secret_key'] = SECRET_KEY_INSECURE_PREFIX + get_random_secret_key()
        config = self.config
        
        print("\n🚀 Project Configuration Summary:")
        for key, value in config.items():
            print(f"{key}: {value}")
            
        confirm = self._yes_no_prompt("\nDo you want to proceed with project creation?", default=True)
        if confirm:
            print(f"\n✨ Creating Django project '{config['project_name']}' in {config['project_path']}")
            if config.get("use_celery", False) == True:
                PROJECT_STRUCTURE['src']['config'][None].append("celery.py")
            if config.get("database") == 'sqlite':
                PROJECT_STRUCTURE['local_db'] = []
                
            folder_generator = FolderGenerator(
                self.config,
                PROJECT_STRUCTURE,
                PROJECT_TEMPLATE_DIR,
            )
            folder_generator.generate()
            
            print(f"Django project '{config['project_name']}' created successfully in {config['project_path']}")
            self.print_success_help()
        else:
            print("Project creation cancelled.")
        
        
def startproject():
    project_structurator = DjangoProjectStructurator()
    project_structurator.generate_project()
