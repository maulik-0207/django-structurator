import sys
import argparse
from importlib.metadata import version, PackageNotFoundError

from django_structurator.commands.startproject import startproject
from django_structurator.commands.startapp import startapp
from django_structurator.helpers.colors import Colors
from django_structurator.settings import DJANGO_PROJECT_FEATURES, DJANGO_APP_FEATURES

class CustomArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        self.print_usage(sys.stderr)
        print(f"{Colors.FAIL}{Colors.BOLD}Error:{Colors.ENDC} {message}\n", file=sys.stderr)
        print(f"Use {Colors.OKCYAN}django-str --help{Colors.ENDC} to see available commands.", file=sys.stderr)
        sys.exit(2)

def info_command(kwargs):
    print(f"\n{Colors.OKBLUE}{Colors.BOLD}Django Structurator CLI{Colors.ENDC}")
    print("A lightweight CLI tool designed to scaffold production-ready Django projects and apps instantly.")
    print("\nAvailable Commands:")
    print("  - startproject : Create a new Django project with best-practice folder structure and Docker support.")
    print("  - startapp     : Create a new Django app with advanced boilerplate (views, models, tasks, APIs).")
    print("  - info         : Display this tool information.")
    print("\nRecommended Workflow:")
    print("  1. Run `django-str startproject` to generate the project shell.")
    print("  2. cd into your new project directory.")
    print("  3. Run `django-str startapp` to scaffold individual apps.")
    print("\nAutomation Examples (Non-Interactive via --no-que):")
    print("  Project: django-str startproject --no-que --name api --path . --db postgresql --use-docker --use-celery")
    print("  App:     django-str startapp --no-que --name billing --use-api-drf --use-tasks-py\n")
    sys.exit(0)

def main():

    try:
        django_structurator_version = version("django_structurator")
    except PackageNotFoundError:
        django_structurator_version = "unknown" 

    main_description = f"""
{Colors.OKBLUE}{Colors.BOLD}Django Structurator CLI (v{django_structurator_version}){Colors.ENDC}

A powerful, AI-friendly CLI tool for rapidly generating robust, 
scalable Django projects and apps without repetitive boilerplate.

Examples:
  Interactive Project Setup:
    $ django-str startproject

  Non-Interactive Project Setup (Full Stack):
    $ django-str startproject --no-que --name myproject --path . --db postgresql --use-docker --use-celery

  Non-Interactive App Setup (API Built-in):
    $ django-str startapp --no-que --name billing --use-api-drf --use-tasks-py

  View System Info:
    $ django-str info
"""

    parser = CustomArgumentParser(
        prog="django-str",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=main_description,
    )
    
    # Add a version option
    parser.add_argument(
        "-v", "--version",
        action="version",
        version=f"Django Structurator CLI {django_structurator_version}",
        help="Show the version of the Django Structurator CLI and exit."
    )

    # subcommands for "startproject" and "startapp"
    subparsers = parser.add_subparsers(
        dest="command",
        title="Commands",
        description="Available operations for scaffolding Django code.",
    )

    # Subcommand: info
    info_parser = subparsers.add_parser(
        "info",
        help="Display general information about the CLI tool and recommended workflow.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="Provides a high-level overview of Django Structurator."
    )

    # Subcommand: startproject
    startproject_desc = """
Generate a Production-Ready Django Project.

Examples:
  Interactive Mode (prompts you for everything):
    $ django-str startproject

  Non-Interactive Mode (Basic Project Profile):
    $ django-str startproject --no-que --name myproject --path ./myproject --db mysql

  Non-Interactive Mode (Heavy production stack with Docker + Database + Broker):
    $ django-str startproject --no-que --name backend_api --path . --db postgresql --use-celery --use-redis --use-docker
"""
    startproject_parser = subparsers.add_parser(
        "startproject",
        help="Create a new Django project with a predefined folder structure.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=startproject_desc,
    )
    startproject_parser.add_argument("--no-que", action="store_true", help="Create project without asking interactive questions.")
    startproject_parser.add_argument("--name", type=str, help="Name of the project (required if --no-que is used).")
    startproject_parser.add_argument("--path", type=str, help="Destination path for the project.")
    startproject_parser.add_argument("--db", type=str, choices=['postgresql', 'mysql', 'sqlite'], help="Database configuration to use (default: sqlite).")
    startproject_parser.add_argument("--env", type=str, choices=['django-environ', 'python-dotenv', 'no_env'], help="Environment variable management (default: django-environ).")
    
    for feature_name, feature_key in DJANGO_PROJECT_FEATURES.items():
        flag = f"--{feature_key.replace('_', '-')}"
        startproject_parser.add_argument(flag, action="store_true", help=f"Include {feature_name} setup.")

    # Subcommand: startapp
    startapp_desc = """
Generate a Structured Django App Template.
Must be run from the root directory of an existing Django project (where manage.py lives).

Examples:
  Interactive Mode:
    $ django-str startapp

  Non-Interactive Mode (Basic Internal App):
    $ django-str startapp --no-que --name users --use-forms-py --use-signals-py

  Non-Interactive Mode (API Microservice with Background Tasks):
    $ django-str startapp --no-que --name billing --use-api-drf --use-tasks-py
"""
    startapp_parser = subparsers.add_parser(
        "startapp",
        help="Create a new Django app with a predefined structure and boilerplates.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=startapp_desc,
    )
    startapp_parser.add_argument("--no-que", action="store_true", help="Create app without asking interactive questions.")
    startapp_parser.add_argument("--name", type=str, help="Name of the app (required if --no-que is used).")
    
    for feature_name, feature_key in DJANGO_APP_FEATURES.items():
        flag = f"--{feature_key.replace('_', '-')}"
        startapp_parser.add_argument(flag, action="store_true", help=f"Include {feature_name} boilerplate.")

    # Parse the arguments
    args = parser.parse_args()
    kwargs = vars(args)

    if args.command == "startproject":
        startproject(kwargs)
    elif args.command == "startapp":
        startapp(kwargs)
    elif args.command == "info":
        info_command(kwargs)
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
