from typing import Callable, List, Optional

class BaseStructurator:
    
    """Common functions used by DjangoProjectStructurator & DjangoAppStructurator."""
    
    def _prompt(
        self, 
        question: str, 
        default: Optional[str]= None, 
        validator: Optional[Callable[[str], str]] = None, 
        options: Optional[List[str]] = None
    ) -> str:
        
        """Ask a question and return the user's validated answer."""
        
        while True:
            # If options are provided, present a menu for selection
            if options:
                print(f"\n{question}")
                for index, option in enumerate(options, start=1):
                    if default and (option == default):
                        print(f"{index}. {option} (default)")
                    else:
                        print(f"{index}. {option}")
                try:
                    user_input = input(f"Select an option (1-{len(options)}): ").strip()

                    # If user presses enter without selection and a default exists
                    if not user_input and default is not None:
                        return default

                    selected_index = int(user_input) - 1
                    if 0 <= selected_index < len(options):
                        return options[selected_index]
                    else:
                        print("Invalid selection. Please choose a valid option.")
                except (ValueError, IndexError):
                    print("Invalid input. Please enter a number corresponding to the options.")
            else:
                # Simple text input prompt
                prompt_message = f"{question}"
                if default is not None:
                    prompt_message += f" (default: {default})"
                prompt_message += ": "

                user_input = input(prompt_message).strip()

                # Use default if no input provided
                if not user_input and default is not None:
                    user_input = default

                # Validate input if validator is provided
                if validator:
                    try:
                        return validator(user_input)
                    except ValueError as e:
                        print(f"Invalid input: {e}")
                        continue
                    except Exception as e:
                        print(f"Unexpected error during validation: {e}")
                        continue
                else:
                    return user_input

    def _yes_no_prompt(
        self, 
        question: str, 
        default: bool = False
    ) -> bool:
        
        """Ask a yes/no question and return a boolean."""
        
        default_str = "y" if default else "n"
        prompt_message = f"{question} (y/n) [default: {default_str}]: "

        while True:
            user_input = input(prompt_message).strip().lower()

            if not user_input:
                return default

            if user_input in ["y", "yes"]:
                return True
            elif user_input in ["n", "no"]:
                return False
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
