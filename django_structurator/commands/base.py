import inquirer


class BaseStructurator:
    
    def _prompt(
        self,
        question: str, 
        default: str = None, 
        validator: callable = None, 
        options: list[str] = None
    ) -> str:
        
        while True:
            if options:
                user_input = inquirer.list_input(
                    message = question, 
                    choices = options,
                )
                return user_input
            else:
                user_input = inquirer.text(
                    message = question,
                    default = default
                )
                
                if validator:
                    try:
                        return validator(user_input)
                    except ValueError as e:
                        print(f"{e}")
                        continue
                return user_input
                    
        
    def _yes_no_prompt(
        self, 
        question: str, 
        default: bool = False,
    ) -> bool:
        
        return inquirer.confirm(question, default=default)
      