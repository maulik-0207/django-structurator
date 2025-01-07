from pathlib import Path


# Useful paths
BASE_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = BASE_DIR / "templates"
APP_TEMPLATES_DIR = TEMPLATES_DIR / "app_template"
PROJECT_TEMPLATE_DIR  = TEMPLATES_DIR / "project_template"


# Settings for project 
PROJECT_NAME_PATTERN = r'^[a-zA-Z][a-zA-Z0-9_]*$'
INVALID_PROJECT_NAME_MESSAGE = "It must start with a letter, and contain only letters, numbers, and underscores."
DISALLOWED_PROJECT_NAMES = []

ENV_CHOICES = ['django-environ', 'python-dotenv', 'no_env']
DEFAULT_ENV = 'django-environ'

DATABASE_CHOICES = ['postgresql', 'mysql', 'sqlite']
DEFAULT_DATABASE = 'sqlite'

DJANGO_PROJECT_FEATURES = {
    # feature_name : feature_key
    'Django Debug Toolbar': 'use_debug_toolbar',
    'Advanced Password Hashers (argon2, bcrypt)': 'use_password_hashers',
    'SMTP Email': 'use_smtp_email',
    'Celery for background tasks': 'use_celery',
    'Redis cache/message broker': 'use_redis',
    'Django Rest Framework (DRF)': 'use_drf',
    'Django Cors Headers': 'use_cors',
}


# Settings for apps 
APP_NAME_PATTERN = r'^[a-z_][a-z0-9_]*$'
INVALID_APP_NAME_MESSAGE = "It must start with a lowercase letter, and contain only lowercase letters, numbers, and underscores."
DISALLOWED_APP_NAMES = []

DJANGO_APP_FEATURES = {
    # feature_name : feature_key
    'forms.py': 'use_forms_py',
    'signals.py': 'use_signals_py',
    'validators.py': 'use_validators_py',
    'tasks.py for Celery tasks' : 'use_tasks_py',
    'template tags/filters' : 'use_template_tags',
    'App level static and template folder' : 'use_app_static_template',
    'API using DRF' : 'use_api_drf',
}