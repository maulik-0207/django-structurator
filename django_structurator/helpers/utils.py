import os
import shutil
from jinja2 import Environment, FileSystemLoader

class FolderGenerator:
    
    def __init__(self, config, folder_structure, template_folder) -> None:
        self.base_path = config.get('project_path') or config.get('base_path')
        self.folder_structure = folder_structure
        self.template_folder = template_folder
        self.config = config
        self.files = dict()
        self.directories = []
        
    def _get_files_directories(self, base_path, folder_structure):
        
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

    def _create_file_from_template(self, file_path, template_path, context):
        # Get the directory of the template
        template_dir = os.path.dirname(template_path)
        template_name = os.path.basename(template_path)

        # Create a Jinja2 environment with the template directory
        env = Environment(loader=FileSystemLoader(template_dir))

        try:
            # Load the template
            template = env.get_template(template_name)

            # Render the template with the provided context
            rendered_content = template.render(context)

            # Create the file and write the rendered content
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(rendered_content)

        except Exception as e:
            print(f"Error: {e}")
    
    def _create_directories(self, directories):
        for directory in directories:
            if not os.path.exists(directory):
                os.mkdir(directory)
    
    def _create_files(self, files):
        for file_path, temp_path in files.items():
            if temp_path and str(temp_path).endswith("-tpl"):
                self._create_file_from_template(file_path, temp_path, self.config)
            elif temp_path and not str(temp_path).endswith("-tpl"):
                shutil.copy(temp_path, file_path)
            else:
                with open(file_path, 'w') as file:
                    file.write("")
    
    def generate(self):
        self._get_files_directories(self.base_path, self.folder_structure)
        self._create_directories(self.directories)
        self._create_files(self.files)