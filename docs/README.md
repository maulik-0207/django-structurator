
<p align="center">
  <img src="https://raw.githubusercontent.com/maulik-0207/django-structurator/master/images/django-structurator_logo.png" alt="django-structurator" width="600"/>
</p>

🚀 **django-structurator** is a lightweight CLI tool that helps you create Django projects and apps with a clean, scalable architecture—without boilerplate or repetitive setup.

No dependencies. No fluff. Just Python `input()` for fast, interactive prompts.

---

## ✅ What It Does

- 📂 Create Django projects with a scalable folder structure.
- ⚙️ Quickly generate Django apps with optional files (forms, signals, validators, API support, etc.).
- 🔧 Customize project setup with advanced features like:
  - Django Rest Framework (DRF)
  - Django Debug Toolbar
  - Celery
  - Redis cache
  - SMTP email config
  - Jazzmin admin
- 🎛️ Auto-generate essential files like `.env.example` and `.gitignore`.

---

## 🚀 Installation

```bash
pip install django-structurator
```

---

## ⚡ Usage

### Create a Django Project

```bash
django-str startproject
```

Follow the prompts to:
- Name your project
- Choose a database: SQLite, PostgreSQL, MySQL
- Pick `.env` configuration (django-environ, python-dotenv)
- Add optional features (DRF, Celery, Redis, Debug Toolbar, etc.)

✅ **Example Output:**
```
>> django-str startproject
Enter project name: test
Enter project path (default: E:\Django\test): 

Select database
1. postgresql
2. mysql
3. sqlite
Select an option (1-3): 3

🔧 Optional Project Features:
Do you want to use Django Debug Toolbar? (y/n) [default: n]: y
....

🚀 Project Configuration Summary:
========================================
project_name: test
project_path: E:\Django\test
database: sqlite
....
========================================

Do you want to proceed with project creation? (y/n) [default: y]: y
...
Django project 'test' created successfully at E:\Django\test
```

---

### Create a Django App

```bash
django-str startapp
```

Follow the prompts to:
- Name your app
- Add files like: `forms.py`, `signals.py`, `validators.py`
- Include optional features like:
  - Template tags/filters
  - Static and templates folders
  - API folder structure (DRF)

✅ **Example Output:**
```
>> django-str startapp    
Enter App name: main

🔧 Optional App Features:
Do you want to use validators.py? (y/n) [default: n]: y
....

🚀 App Configuration Summary:
app_dir: ...\test\src\apps
app_name: main
app_path: ...\test\src\apps\main
use_validators_py: True
....

Do you want to proceed with app creation? (y/n) [default: y]: y

🎉 Django app 'main' created successfully!
```

---

## 🏗️ Example Project Structure

```plaintext
my_project/
├── docs/
├── local_db/
├── requirements/
├── src/
│   ├── apps/
│   │   ├── blog/
│   │   │   ├── api/v1/
│   │   │   ├── migrations/
│   │   │   ├── templatetags/
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── forms.py
│   │   │   ├── models.py
│   │   │   ├── signals.py
│   │   │   ├── tasks.py
│   │   │   ├── validators.py
│   │   │   └── views.py
│   │   └── ...
│   ├── common/
│   ├── config/
│   │   ├── settings/
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   ├── media/
│   ├── static/
│   ├── templates/
│   └── manage.py
└── .gitignore
```

---

## ✅ Requirements

- Python 3.8+
- Django 3.2+

---

## 📄 License

MIT License - See the [LICENSE](https://github.com/maulik-0207/django-structurator/blob/main/LICENSE)

---

## 🔗 Links

- GitHub Repo: [maulik-0207/django-structurator](https://github.com/maulik-0207/django-structurator)
- PyPI Package: [django-structurator](https://pypi.org/project/django-structurator/)


---

## Why Use django-structurator?

🔥 **Save time**, avoid repetitive setup  
🧹 Clean, maintainable architecture  
⚡ Lightweight, no external dependencies  
🛠️ Customizable project and app scaffolding  
