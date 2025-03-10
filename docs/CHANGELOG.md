# Changelog

All notable changes to the `django-structurator` project will be documented in this file. This project adheres to [Semantic Versioning](https://semver.org/).

---

## Format Guide

- **Added**: New features or functionality.
- **Changed**: Updates to existing functionality or improvements.
- **Deprecated**: Features marked for removal in future releases.
- **Removed**: Features or functionality removed in this release.
- **Fixed**: Bug fixes or issues resolved.
- **Security**: Updates related to security improvements.

---

## [1.1.0] - 2025-03-10

### Changed
- Updated project and app templates content.

### Removed
- CLI interaction with inquirer is removed to make package more lightweight.
- Removed USAGE.md and TROUBLESHOOTING.md from templates.

### Fixed
- Fixed issue with signals in AppConfig file template.


---

## [1.0.0] - 2025-01-08

### Added
- Improved code quality with type hinting and docstrings.
- Added `django-cors-headers` for Cross-Origin Resource Sharing (CORS) management.
- Integrated Jazzmin for customizable Django admin panel skins.
- Enhanced project and template documentation.
- Improved overall project structure and feature set.

---

## [0.1.2] - 2024-12-17

### Added
- Switched from Jinja2 to Django templates for project generation.
- Introduced `inquirer` for better interactive user inputs.
- Added detailed documentation templates for Django files.
- Introduced additional environment choices during project initialization.
- Included several new features and configurations.

---

## [0.1.1] - 2024-12-08

### Added
- Support for SMTP Email configuration.
- Integrated Celery for background task management.
- Added support for app-level `static/` and `templates/` folders.

### Fixed
- Addressed bugs related to project initialization and structure creation.

---

## [0.1.0] - 2024-12-06

### Added
- Initial release of `django-structurator`.
- Basic folder structure for Django project, including `src/`, `apps/`, and `config/` directories.
- Support for environment-specific settings (`base.py`, `development.py`, `production.py`).
- Included `media/`, `static/`, and `templates/` directories for file organization.
- Basic CLI commands (`django-str`) for project and app initialization.
- Documentation templates for `README.md`, `ARCHITECTURE.md`, and `CHANGELOG.md`.

---
