import os
import shutil
from django.template import Context, Template
from django.conf import settings
from django import setup


class FolderGenerator:
    
    """Class to create any kind of folder structure with provided context data and template folder.
    """    
    
    def __init__(
        self, 
        config: dict, 
        folder_structure: dict, 
        template_folder: str
    ) -> None:
        self.base_path = config.get('project_path') or config.get('app_path') or config.get('base_path') 
        self.folder_structure = folder_structure
        self.template_folder = template_folder
        self.config = config
        self.files = dict()
        self.directories = []
        
    def _get_files_directories(self, base_path: str, folder_structure: dict) -> None:
        """This function will find path of all files & directories and store it to class level files & directories variables.
        """        
        for folder, content in folder_structure.items():
            if folder == None:
                folder_path = base_path
                folder = ""
            else:
                folder_path = os.path.join(base_path, folder)
            
            # Create the folder
            if not folder_path in self.directories:
                self.directories.append(folder_path)
            
            
            # If the folder contains files, create them
            if isinstance(content, list):
                for file_name in content:
                    file_path = os.path.join(folder_path, file_name)
                    
                    template_path = os.path.join(self.template_folder, os.path.relpath(file_path, self.base_path) + '-tpl')

                    if os.path.exists(template_path):
                        self.files[file_path] = template_path
                    elif os.path.exists(os.path.join(self.template_folder, os.path.relpath(file_path, self.base_path))):
                        self.files[file_path] = os.path.join(self.template_folder, os.path.relpath(file_path, self.base_path))
                    else:
                        self.files[file_path] = None
            
            # If the folder is a dictionary, it means it has subfolders to create
            elif isinstance(content, dict):
                self._get_files_directories(folder_path, content)

    def _create_file_from_template(self, file_path: str, template_path: str, context: dict) -> None:
        """This function will create file from template file and context data using Django Template Engine.
        """        
        try:
            if not settings.configured:
                settings.configure(
                    TEMPLATES=[
                        {
                            "BACKEND": "django.template.backends.django.DjangoTemplates",
                            "DIRS": [],
                            "APP_DIRS": False,
                            "OPTIONS": {},
                        }
                    ]
                )
                setup()
            
            # Read the template content
            with open(template_path, "r", encoding="utf-8") as template_file:
                template_content = template_file.read()

            # Create a Django Template object
            template = Template(template_content)

            # Render the template with the provided context
            rendered_content = template.render(Context(context))

            # Create the file and write the cleaned content
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(rendered_content)

        except Exception as e:
            print(f"An error occured during creation of file : {file_path}")
            print(f"Error: {e}\n")
    
    def _create_directories(self, directories: list) -> None:
        """This function will create all directories provided in the list. 
        """
        for directory in directories:
            if not os.path.exists(directory):
                os.mkdir(directory)
    
    def _create_files(self, files: dict) -> None:
        """This function will take file path in key and template path in value.
        If template path and ends with -tpl: it will create file from template and context data.
        If template path and doesn't end with -tpl: it will copy template to file location.
        If template path is None: it will create empty file.
        """
        for file_path, temp_path in files.items():
            if temp_path and str(temp_path).endswith("-tpl"):
                self._create_file_from_template(file_path, temp_path, self.config)
            elif temp_path and not str(temp_path).endswith("-tpl"):
                shutil.copy(temp_path, file_path)
            else:
                with open(file_path, 'w') as file:
                    file.write("")
    
    def generate(self) -> None:
        """This function will use all above functions to create provided folder structure.
        """
        self._get_files_directories(self.base_path, self.folder_structure)
        self._create_directories(self.directories)
        self._create_files(self.files)
