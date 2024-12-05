from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = BASE_DIR / "templates"
APP_TEMPLATES_DIR = TEMPLATES_DIR / "app_template"
PROJECT_TEMPLATE_DIR  = TEMPLATES_DIR / "project_template"

PROJECT_NAME_PATTERN = r'^[a-zA-Z][a-zA-Z0-9_]*$'
DISALLOWED_PROJECT_NAMES = []

DATABASE_CHOICES = ['postgresql', 'mysql', 'sqlite']
DEFAULT_DATABASE = 'sqlite'

DJANGO_PROJECT_FEATURES = {
    # feature_name : feature_key
    'Advanced Password Hashers (argon2, bcrypt)': 'use_password_hashers',
    'Configure SMTP Email': 'use_smtp_email',
    'Django Debug Toolbar': 'use_debug_toolbar',
    'Redis cache/message broker': 'use_redis',
    'Celery for background tasks': 'use_celery',
    'Django Rest Framework (DRF)': 'use_drf',
}


APP_NAME_PATTERN = r'^[a-z_][a-z0-9_]*$'
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