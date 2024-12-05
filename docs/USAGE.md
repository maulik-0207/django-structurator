# Django Structurator Usage Guide

## Installation

```bash
pip install django-structurator
```

## Project Creation

### Basic Usage
```bash
django-str startproject
```

### Interactive Prompts
- Enter project name
- Select project path
- Choose database
- Configure optional features

## App Creation

### Basic Usage
```bash
django-str startapp
```

### Interactive Prompts
- Enter app name
- Select app features

## Configuration Options

### Project Features
- Password Hashers
- SMTP Email
- Debug Toolbar
- Redis
- Celery
- Django Rest Framework

### App Features
- Forms
- Signals
- Validators
- Celery Tasks
- Template Tags
- Static Folders
- DRF API

## Example Workflow

1. Create Project
```bash
django-str startproject
# Follow interactive prompts
```

2. Create App
```bash
django-str startapp
# Follow interactive prompts
```

## Customization
- Modify templates in project structure
- Add custom feature flags
- Extend validation logic