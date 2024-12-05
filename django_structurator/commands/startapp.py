import os
import re
import sys
from sys import platform
from django_structurator.helpers.structures import APP_STRUCTURE
from django_structurator.helpers.utils import FolderGenerator
from django_structurator.settings import (
    DISALLOWED_APP_NAMES,
    APP_NAME_PATTERN,
    DJANGO_APP_FEATURES,
    APP_TEMPLATES_DIR
)


class DjangoAppStructurator:
    
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
    
    def _app_name_validator(self, name):
        if not name:
            raise ValueError("App name cannot be empty.")

        if not re.match(APP_NAME_PATTERN, name):
            raise ValueError(
                "It must start with a letter, "
                "and contain only lowercase letters, numbers, and underscores."
            )
        
        # Check against reserved keywords and disallowed names
        import keyword
        if name in keyword.kwlist:
            raise ValueError(f"Invalid app name. '{name}' is a reserved Python keyword.")
        
        # Check if the name matches common disallowed names
        if name.lower() in DISALLOWED_APP_NAMES:
            raise ValueError(f"Invalid app name. '{name}' is disallowed.")
        
        if os.path.exists(os.path.join(self.config.get('app_dir'), str(name))):
            raise ValueError(f"An app/folder with the name '{name}' already exists at {self.config.get('app_dir')}.")
        
        return name
    
    def _check_project_structure(self):
        if not os.path.exists('manage.py'):
            print("❌ Error: Not in a Django project root directory.")
            print("Please run this script from your Django project's root directory where 'manage.py' is situated.")
            sys.exit(1)
    
    def _get_app_configurations(self):
        self._check_project_structure()
        
        app_dir = os.path.join(os.getcwd(), 'apps')
        self.config['app_dir'] = app_dir
        
        app_name = self._prompt(
            "Enter App name", 
            validator= self._app_name_validator
        )
        self.config['app_name'] = app_name

        app_path = os.path.join(self.config.get('app_dir'), app_name)
        self.config['base_path'] = app_path
        
        print("\n🔧 Optional App Features:")
        for feature, feature_key in DJANGO_APP_FEATURES.items():
            self.config[feature_key] = self._yes_no_prompt(
                f"Do you want to use {feature}?", 
                default=False
            )
    
    def _print_windows_success_help(self):
        app_name = self.config.get("app_name")
        
        print("\n🌟 Next Steps for Your Django Application:")
        step_no = 1
        print("\n1. Add the app to your INSTALLED_APPS in `base.py` of settings/ inside config/:")
        print(f"   'apps.{app_name}',")
        step_no += 1
        
        print("\n2. Add the app's urls to project level urls.py:")
        print(f"   path('{app_name}/',include('apps.{app_name}.urls')),")
        step_no += 1
        
        if self.config.get("use_api_drf"):
            print(f"\n{step_no}. Add API URL to your project's `urls.py`:")
            print(f"   path('api/v1/{app_name}/', include('apps.{app_name}.api.v1.urls')),")
            step_no += 1
        
        # If other features are enabled, provide additional instructions
        if self.config.get("use_tasks_py"):
            print(f"\n{step_no}. Set up Celery for background tasks:")
            print("   - Ensure Celery is properly configured in your Django project. Check the Celery documentation for setup instructions.")
            step_no += 1

        print("\n🌍 Finally, you can start your Django development server using `python manage.py runserver`.")
    
    def _print_unix_success_help(self):
        app_name = self.config.get("app_name")
        
        print("\n🌟 Next Steps for Your Django Application:")
        step_no = 1
        print("\n1. Add the app to your INSTALLED_APPS in `base.py` of settings/ inside config/:")
        print(f"   'apps.{app_name}',")
        step_no += 1
        
        print("\n2. Add the app's urls to project level urls.py:")
        print(f"   path('{app_name}/',include('apps.{app_name}.urls')),")
        step_no += 1
        
        if self.config.get("use_api_drf"):
            print(f"\n{step_no}. Add API URL to your project's `urls.py`:")
            print(f"   path('api/v1/{app_name}/', include('apps.{app_name}.api.v1.urls')),")
            step_no += 1
        
        # If other features are enabled, provide additional instructions
        if self.config.get("use_tasks_py"):
            print(f"\n{step_no}. Set up Celery for background tasks:")
            print("   - Ensure Celery is properly configured in your Django project. Check the Celery documentation for setup instructions.")
            step_no += 1

        print("\n🌍 Finally, you can start your Django development server using `python manage.py runserver`.")
     
    def print_success_help(self):
        if platform == "darwin" or platform == "linux" or platform == "linux2":  # macOS
            self._print_unix_success_help()
        elif platform == "win32":   # Windows... 
            self._print_windows_success_help()
        else:
            self._print_windows_success_help()
    
    def generate_app(self):
        
        self._get_app_configurations()
        config = self.config
        
        print("\n🚀 App Configuration Summary:")
        for key, value in config.items():
            print(f"{key}: {value}")
            
        confirm = self._yes_no_prompt("\nDo you want to proceed with app creation?", default=True)
        if confirm:
            print(f"\n✨ Creating Django app '{config['app_name']}'")
            
            if config.get("use_forms_py") == True:
                APP_STRUCTURE[None].append("forms.py")
            
            if config.get("use_signals_py") == True:
                APP_STRUCTURE[None].append("signals.py")
            
            if config.get("use_validators_py") == True:
                APP_STRUCTURE[None].append("validators.py")
            
            if config.get("use_tasks_py") == True:
                APP_STRUCTURE[None].append("tasks.py")
            
            if config.get("use_template_tags") == True:
                APP_STRUCTURE['templatetags'] = ['__init__.py', 'exampleFilter.py', 'exampleTag.py']
                
            if config.get("use_app_static_template") == True:
                APP_STRUCTURE['templates'] = {str(config['app_name']): []}
                APP_STRUCTURE['static'] = {str(config['app_name']): {'images': [], 'css': [], 'js': []}}
                
            if config.get("use_api_drf") == True:
                APP_STRUCTURE['api'] = {
                    None: ['__init__.py'],
                    'v1': ['__init__.py', 'serializers.py', 'urls.py', 'views.py']
                }
                APP_STRUCTURE['static'] = {str(config['app_name']): {'images': [], 'css': [], 'js': []}}
                        
            folder_generator = FolderGenerator(
                self.config,
                APP_STRUCTURE,
                APP_TEMPLATES_DIR,
            )
            
            folder_generator.generate()
            
            print(f"\n🎉 Django app '{config['app_name']}' created successfully!")
            self.print_success_help()
        else:
            print("App creation cancelled.")
        
        
def startapp():
    app_structurator = DjangoAppStructurator()
    app_structurator.generate_app()