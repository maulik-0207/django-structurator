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

## [1.3.0] - 2026-04-15

### Added

- Feature for fully automated / non-interactive CLI generations using the `--no-que` flag across both `startproject` and `startapp`.
- Introduced the `django-str info` subcommand to outline project workflows.
- Rich, colored CLI outputs for detailed terminal-based scaffolding success summaries and error warnings.
- Explicit Docker configurations natively generated (`Dockerfile`, `docker-compose.yml`, `nginx/`) using the `--use-docker` toggle.
- Comprehensive `AI_CONTEXT.md` and `ARCHITECTURE.md` generation structures crafted to safely guide AI code generation tools.
- Advanced Database Isolation Test Cases boilerplate embedded into `tests.py`.
- Dynamic environments configuration logic injected safely into `wsgi.py`, `asgi.py`, and `manage.py` for seamless transitions between `.env` states (`development` vs `production`).
- TimeStampedUUIDModel explicitly built as an abstract class in generated `models.py`.

### Changed

- Improved overall package modularity and `PEP-8` compliant code quality of the scaffolding generator files (Stateless `copy.deepcopy` logic injected for structural templates).
- Overhauled `cli.py` using `argparse.RawDescriptionHelpFormatter` to deliver extensive feature mapping within `--help` commands.
- Updated core Django boilerplates across `views.py`, `urls.py`, and `settings/base.py` for improved readability.
- Made Django `debug_toolbar` a mandatory and standard component of the `development.py` environment stack.
- Dynamic root level layout creation (Folders like `local_db/` and `logs/` are explicitly instantiated during skeleton build).

### Removed

- Removed the `no_env` option. Environment management handling (`python-dotenv` or `django-environ`) is now mandatory for creating projects to enforce secure secret policies.
- Deprecated multiple redundant CLI flag arguments (such as explicit form toggles) resulting in cleaner, enforced boilerplate structures.

---

## [1.2.1] - 2025-07-24

### Fixed

- Fixed Error of `src/config/settings/base.py` by adding LevelFilter class.

---

## [1.2.0] - 2025-07-21

### Added

- Added better content into `README.md` file for project setup.
- Added option for use of `Custom Django Logger` while porject creation.
- Started using logger instead of print in send_mail() of helpers.py in common folder.

### Changed

- Made `DISALLOWED_PROJECT_NAMES` list empty.
- Changed default content of some template files.

### Fixed

- Fixed issues with `Celery` implementation.
- Fixed issue with `pkg_resources` by replacing it with `importlib`.

---

## [1.1.1] - 2025-06-23

### Changed

- Updated project and app templates content.

### Fixed

- Fixed issue with selection of options while project/app creatation.

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
