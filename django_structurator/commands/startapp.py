import os
import re
import sys
import copy
import keyword
from django_structurator.commands.base import BaseStructurator
from django_structurator.helpers.structures import APP_STRUCTURE
from django_structurator.helpers.utils import FolderGenerator
from django_structurator.settings import (
    APP_TEMPLATES_DIR,
    APP_NAME_PATTERN,
    INVALID_APP_NAME_MESSAGE,
    DISALLOWED_APP_NAMES,
    DJANGO_APP_FEATURES
)
from django_structurator.helpers.colors import Colors


class DjangoAppStructurator(BaseStructurator):
    
    """Class to create Django App with user choices and best folder structure.
    """
    
    def __init__(self, kwargs=None) -> None:
        self.config = {}
        self.kwargs = kwargs or {}

    def _check_project_path(self) -> None:
        """Function to check that command is running from project root directory so it can find apps directory easily.
        """
        
        if not os.path.exists('manage.py'):
            print("❌ Error: Not in a Django project root directory.")
            print("Please run this script from your Django project's root directory where 'manage.py' is situated.")
            sys.exit(1)

    def _app_name_validator(self, name: str) -> None:
        """Validator for App Name.
        """
        
        if not name:
            raise ValueError("App name cannot be empty.")

        if not re.match(APP_NAME_PATTERN, name):
            raise ValueError(
                INVALID_APP_NAME_MESSAGE
            )
        
        # Check against reserved keywords and disallowed names
        if name in keyword.kwlist:
            raise ValueError(f"Invalid app name. '{name}' is a reserved Python keyword.")
        
        # Check if the name matches common disallowed names
        if name.lower() in DISALLOWED_APP_NAMES:
            raise ValueError(f"Invalid app name. '{name}' is disallowed.")
        
        if os.path.exists(os.path.join(self.config.get('app_dir'), str(name))):
            raise ValueError(f"An app/folder with the name '{name}' already exists at {self.config.get('app_dir')}.")
        
        return name
    
    def _get_app_configurations(self) -> None:
        """This function will take all user choices and store it into class level config variable.
        """
        
        self._check_project_path()
        
        app_dir = os.path.join(os.getcwd(), 'apps')
        self.config['app_dir'] = app_dir
        
        if self.kwargs and self.kwargs.get('no_que'):
            app_name = self.kwargs.get('name')
            if not app_name:
                print("Error: --name is required when using --no-que")
                sys.exit(1)
            self.config['app_name'] = self._app_name_validator(app_name)
            self.config['app_path'] = os.path.join(self.config.get('app_dir'), self.config['app_name'])
            
            for feature, feature_key in DJANGO_APP_FEATURES.items():
                self.config[feature_key] = self.kwargs.get(feature_key, False)
            return

        app_name = super()._prompt(
            "Enter App name", 
            validator= self._app_name_validator
        )
        self.config['app_name'] = app_name

        app_path = os.path.join(self.config.get('app_dir'), app_name)
        self.config['app_path'] = app_path
        
        print("\n🔧 Optional App Features:")
        for feature, feature_key in DJANGO_APP_FEATURES.items():
            self.config[feature_key] = super()._yes_no_prompt(
                f"Do you want to use {feature}?", 
                default=False
            )
     
    def print_success_help(self) -> None:
        """This function will print next steps for user after creation of new Django app.
        """
        
        app_name = self.config.get("app_name")
        
        print(f"\n{Colors.OKGREEN}{Colors.BOLD}🌟 Next Steps for Your Django Application:{Colors.ENDC}")
        step_no = 1
        print(f"\n{Colors.OKCYAN}{step_no}. Add the app to your INSTALLED_APPS in `base.py` of settings/ inside config/:{Colors.ENDC}")
        print(f"   {Colors.WARNING}'apps.{app_name}',{Colors.ENDC}")
        step_no += 1
        
        print(f"\n{Colors.OKCYAN}{step_no}. Add the app's urls to project level urls.py:{Colors.ENDC}")
        print(f"   {Colors.WARNING}path('{app_name}/',include('apps.{app_name}.urls')),{Colors.ENDC}")
        step_no += 1
        
        if self.config.get("use_api_drf"):
            print(f"\n{Colors.OKCYAN}{step_no}. Add API URL to your project's `urls.py`:{Colors.ENDC}")
            print(f"   {Colors.WARNING}path('api/v1/{app_name}/', include('apps.{app_name}.api.v1.urls')),{Colors.ENDC}")
            step_no += 1
    
    def generate_app(self) -> None:
        """This function will use all above function to create Django app with user choices.
        """
        
        self._get_app_configurations()
        config = self.config
        
        print("\n🚀 App Configuration Summary:")
        for key, value in config.items():
            print(f"{key}: {value}")
        
        print("")            
        if self.kwargs and self.kwargs.get('no_que'):
            confirm = True
        else:
            confirm = super()._yes_no_prompt("Do you want to proceed with app creation?", default=True)
        if confirm:
            import copy
            app_structure = copy.deepcopy(APP_STRUCTURE)
            
            if config.get("use_forms"):
                app_structure[None].append("forms.py")
            
            if config.get("use_signals"):
                app_structure[None].append("signals.py")
            
            if config.get("use_tasks"):
                app_structure[None].append("tasks.py")
            
            if config.get("use_app_static_template"):
                app_structure['templates'] = {str(config['app_name']): []}
                app_structure['static'] = {str(config['app_name']): {'images': [], 'css': [], 'js': []}}
            
            if config.get("use_template_tags"):
                app_structure['templatetags'] = ['__init__.py', 'example_filter.py', 'example_tag.py']
                
            if config.get("use_api_drf"):
                app_structure['api'] = {
                    None: ['__init__.py'],
                    'v1': ['__init__.py', 'serializers.py', 'urls.py', 'views.py']
                }
                   
            folder_generator = FolderGenerator(
                self.config,
                app_structure,
                APP_TEMPLATES_DIR,
            )
            
            folder_generator.generate()
            
            print(f"\n{Colors.OKGREEN}🎉 Django app '{config['app_name']}' created successfully!{Colors.ENDC}")
            self.print_success_help()
        else:
            print("App creation cancelled.")

        
def startapp(kwargs=None):
    app_structurator = DjangoAppStructurator(kwargs)
    app_structurator.generate_app()
