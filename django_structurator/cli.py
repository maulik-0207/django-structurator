from django_structurator.commands.startproject import startproject
from django_structurator.commands.startapp import startapp

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Django Structurator CLI")
    parser.add_argument(
        "command", 
        choices=["startproject", "startapp"], 
        help="Command to execute: startproject"
    )

    args = parser.parse_args()

    if args.command == "startproject":
        startproject()
    elif args.command == "startapp":
        startapp()
