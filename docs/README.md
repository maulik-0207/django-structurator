
<p align="center">
  <img src="https://raw.githubusercontent.com/maulik-0207/django-structurator/master/images/django-structurator_logo.png" alt="django-structurator" width="600"/>
</p>

🚀 **django-structurator** is a lightweight CLI tool that helps you create Django projects and apps with a clean, scalable architecture—without boilerplate or repetitive setup.

No extra dependencies. No bloated templates. Just a clean, prompt-driven workflow.

---

## ⚙️ Features

- 📁 **Scalable Folder Structure** – Consistent architecture for better maintainability.
- 🧩 **Modular App Generation** – Create Django apps with optional files: `forms`, `signals`, `validators`, `tasks`, and more.
- 🔌 **Optional Add-ons**:
  - Django REST Framework (DRF)
  - Django Debug Toolbar
  - Celery + Redis
  - SMTP Email Configuration
  - Jazzmin Admin UI
  - Custom Django Logger
- 📄 Auto-generates essentials: `.env.example`, `.gitignore`, `requirements/`, and more.

---

## 📦 Installation

```bash
pip install django-structurator
```

---

## ⚡ Usage

### 📂 Create a New Django Project

```bash
django-str startproject
```

Interactive CLI will ask:
- Project name and path
- Database: SQLite / PostgreSQL / MySQL
- `.env` management: `django-environ` / `python-dotenv`
- Optional integrations (Debug Toolbar, DRF, Celery, Redis, Logger etc.)

### 🧱 Create a New Django App

```bash
django-str startapp
```

CLI will prompt for:
- App name
- Optional modules: `forms.py`, `signals.py`, `validators.py`
- Include optional features like:
  - Template tags/filters
  - Static and templates folders
  - API folder structure (DRF)

---

## 🏗️ Example Project Structure

```plaintext
test/ 
│
├── docs/                     # Documentation files
│   ├── ARCHITECTURE.md       # Project folder architecture guide
│   ├── CHANGELOG.md          # Change log for the project
│   └── README.md             # Main documentation file
│
├── local_db/                 # Local SQLite database for development
│   └── db.sqlite3
│
├── logs/                     # Every level Log files will be here
│   ├── critical.log      
│   ├── debug.log          
│   ├── error.log          
│   ├── info.log          
│   └── warning.log             
|
├── requirements/             # Dependency management
│   ├── base.txt              # Core dependencies
│   ├── development.txt       # Development-specific dependencies
│   ├── production.txt        # Production-specific dependencies
│   └── test.txt              # Testing dependencies
│
├── src/                      # Main source code folder
│   ├── apps/                 # All Django apps
|   |   ├── app-1/                    # Example Django app
|   |   │   │
|   |   │   ├── api/                  # API for app-1
|   |   │   │   ├── v1/               # Version 1 of the API
|   |   │   │   │   ├── __init__.py
|   |   │   │   │   ├── serializers.py # Serializers for API data
|   |   │   │   │   ├── urls.py        # API URL patterns
|   |   │   │   │   └── views.py       # API views
|   |   │   │   └── __init__.py
|   |   │   │
|   |   │   ├── migrations/           # Database migrations
|   |   │   │   └── __init__.py
|   |   │   │
|   |   │   ├── templatetags/         # Custom template tags and filters
|   |   │   │   ├── __init__.py
|   |   │   │   ├── example_filter.py # Custom filter example
|   |   │   │   └── example_tag.py    # Custom tag example
|   |   │   │
|   |   │   ├── __init__.py
|   |   │   ├── admin.py              # Admin site configuration
|   |   │   ├── apps.py               # App configuration
|   |   │   ├── forms.py              # App-specific forms (optional)
|   |   │   ├── models.py             # App models
|   |   │   ├── signals.py            # Signal handlers (optional)
|   |   │   ├── tasks.py              # Celery tasks (optional)
|   |   │   ├── tests.py              # Unit tests
|   |   │   ├── urls.py               # App-specific URL patterns
|   |   │   ├── validators.py         # Custom validators (optional)
|   |   │   └── views.py              # App views
|   |   │
|   |   ├── app-2/                    # Another app
|   |   ├── app-3/
|   |   ├── ...
|   |   └── app-4/
│   │
│   ├── common/               # Shared utilities, constants, and helpers
│   │   ├── __init__.py
│   │   ├── constants.py      # Commonly used constants
│   │   └── helpers.py        # Utility functions
│   │
│   ├── config/               # Project configuration
│   │   ├── settings/         # Environment-specific settings
│   │   │   ├── __init__.py
│   │   │   ├── base.py       # Base settings
│   │   │   ├── development.py # Development environment settings
│   │   │   └── production.py # Production environment settings
│   │   ├── __init__.py
│   │   ├── .env              # Environment variables (in config directory)
│   │   ├── .env.example      # Example env file (in config directory)
│   │   ├── asgi.py           # ASGI configuration
│   │   ├── celery.py         # Celery configuration file if used
│   │   ├── urls.py           # URL configuration
│   │   └── wsgi.py           # WSGI configuration
│   │
│   ├── media/                # Uploaded media files
│   │
│   ├── static/               # Static files
│   │   ├── css/              # CSS files
│   │   ├── js/               # JavaScript files
│   │   └── images/           # Image files
│   │       └── favicon.ico   # Favicon
│   │
│   ├── templates/            # HTML templates
│   │   ├── base.html         # Base HTML template
│   │   └── index.html        # Default landing page template
│   │
│   └── manage.py             # Django's management script
│
└── .gitignore                # Git ignore file
```

---

## ✅ Requirements

- Python 3.8+
- Django 3.2+

---

## 🧠 Why Use It?

- 🔥 Save time and skip repetitive setup

- 🧼 Enforce consistency across teams

- ⚡ Fast, interactive, zero-bloat generator

---

## 📄 License

MIT License - See the [LICENSE](https://github.com/maulik-0207/django-structurator/blob/main/LICENSE)

---

## 🔗 Links

- GitHub Repo: [maulik-0207/django-structurator](https://github.com/maulik-0207/django-structurator)
- PyPI Package: [django-structurator](https://pypi.org/project/django-structurator/)
