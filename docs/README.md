<p align="center">
  <img src="https://raw.githubusercontent.com/maulik-0207/django-structurator/master/images/django-structurator_logo.png" alt="django-structurator" width="600"/>
</p>

🚀 **django-structurator** is an incredibly powerful, AI-friendly CLI tool designed to scaffold production-ready Django projects and apps instantly. It enforces a strict, scalable architecture out of the box, eliminating repetitive boilerplate and creating a highly modular environment.

Whether you're a human developer looking for consistency or an **AI Coding Assistant** (like Cursor, Claude, or Antigravity) seeking explicit structural rules, this package lays down a flawless foundation. No extra dependencies. No bloated templates. Just a clean, prompt-driven workflow.

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

**Interactive Mode:**

```bash
django-str startproject
```

**Non-Interactive Mode (Full Stack Automation):**

```bash
django-str startproject --no-que --name myproject --path . --env django-environ --db postgresql --use-docker --use-celery
```

The CLI natively supports configuring:

- Database: SQLite / PostgreSQL / MySQL
- Environments: `django-environ` / `python-dotenv`
- Optional Integrations: use-smtp-email, use-celery, use-redis, use-drf, use-jazzmin, use-logger, use-docker

### 🧱 Create a New Django App

App generation must be executed from the root of an existing Django project (where `manage.py` lives).

**Interactive Mode:**

```bash
django-str startapp
```

**Non-Interactive Mode (API Microservice):**

```bash
django-str startapp --no-que --name billing --use-api-drf --use-tasks
```

Optional App-level Modules:

- use-forms, use-signals, use-tasks, use-app-static-template, use-template-tags, use-api-drf

---

## 🏗️ Example Project Structure

````plaintext
```text
my_project/
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
│
├── nginx/                    # Optional: Nginx reverse proxy configuration
│   └── nginx.conf
│
├── docker-compose.yml        # Optional: Docker map (web, db, redis, celery)
├── Dockerfile                # Optional: Docker web container configuration
│
├── requirements/             # Dependency management
│   ├── base.txt              # Core dependencies
│   ├── development.txt       # Development-specific dependencies
│   ├── production.txt        # Production-specific dependencies
│   └── test.txt              # Testing dependencies
│
├── src/                      # Main source code folder
│   ├── apps/                 # All Django apps
│   │   ├── app-1/            # Example Django app
│   │   │   │
│   │   │   ├── api/          # API for app-1
│   │   │   │   ├── v1/       # Version 1 of the API
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── serializers.py
│   │   │   │   │   ├── urls.py
│   │   │   │   │   └── views.py
│   │   │   │   └── __init__.py
│   │   │   │
│   │   │   ├── migrations/   # Database migrations
│   │   │   │
│   │   │   ├── templatetags/ # Custom template tags and filters
│   │   │   │
│   │   │   ├── admin.py      # Admin site configuration
│   │   │   ├── apps.py       # App configuration
│   │   │   ├── models.py     # App models (Abstracts TimeStamped UUID)
│   │   │   ├── tests.py      # Isolated DB test cases
│   │   │   ├── urls.py       # App-specific URL patterns
│   │   │   └── views.py      # App views
│   │   │
│   │   ├── app-2/            # Another app
│   │   └── ...
│   │
│   ├── common/               # Shared utilities, constants, and helpers
│   │   ├── __init__.py
│   │   ├── constants.py      # Commonly used constants
│   │   └── helpers.py        # Utility functions (mailer, loggers)
│   │
│   ├── config/               # Project configuration
│   │   ├── settings/         # Environment-specific settings
│   │   │   ├── __init__.py
│   │   │   ├── base.py       # Base settings
│   │   │   ├── development.py # Development environment settings
│   │   │   └── production.py # Production environment settings
│   │   ├── .env              # Environment secrets boundary
│   │   ├── .env.example      # Example env file
│   │   ├── asgi.py           # ASGI configuration
│   │   ├── celery.py         # Celery configuration file
│   │   ├── urls.py           # Master URL configuration
│   │   └── wsgi.py           # WSGI configuration
│   │
│   ├── media/                # Uploaded media files
│   ├── static/               # Static files
│   ├── templates/            # Global HTML templates
│   └── manage.py             # Django's management script
│
└── .gitignore                # Git ignore file
````

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
