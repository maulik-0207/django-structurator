from importlib.metadata import version, PackageNotFoundError
from django_structurator.commands.startproject import startproject
from django_structurator.commands.startapp import startapp

def main():
    import argparse
    import sys

    parser = argparse.ArgumentParser(
        description="A lightweight CLI tool that helps you create Django projects and apps with a clean, scalable architecture—without boilerplate or repetitive setup.",
    )
    
    try:
        django_structurator_version = version("django_structurator")
    except PackageNotFoundError:
        django_structurator_version = "unknown" 
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
        title="Available Commands",
        description="Commands to create Django projects or apps.",
    )

    # Subcommand: startproject
    subparsers.add_parser(
        "startproject",
        help="Create a new Django project with a predefined folder structure."
    )

    # Subcommand: startapp
    subparsers.add_parser(
        "startapp",
        help="Create a new Django app with a predefined folder structure."
    )

    # Parse the arguments
    args = parser.parse_args()

    if args.command == "startproject":
        startproject()
    elif args.command == "startapp":
        startapp()
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
