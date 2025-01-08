from django_structurator.commands.startproject import startproject
from django_structurator.commands.startapp import startapp

__version__ = "1.0.0"

def main():
    import argparse
    import sys

    parser = argparse.ArgumentParser(
        description="Django Structurator CLI - A tool to help you quickly create structured Django projects and apps.",
    )

    # Add a version option
    parser.add_argument(
        "-v", "--version",
        action="version",
        version=f"Django Structurator CLI {__version__}",
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
