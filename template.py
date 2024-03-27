import os
from pathlib import Path
import logging 

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] - [%(levelname)s]:  %(message)s:')

project_name = "textSummarizerOlmo7B" 

# Folder structure
list_of_files = [
    # CI/CD related yaml files 
    # Commit in github -> Automatically push commit changes to cloud
    ".github/workflows/.gitkeep", 

    # __init__.py tells Python that this folder is a package 
    # Allows modules within the folder to be imported under a single package namespace
    # ex: from {project_name}.{module_name} import {function_name} in a Jupyter Notebook
    f"src/{project_name}/__init__.py", 
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py", 
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "experiments/trials.ipynb",
    "test.py"
] 

for filepath in list_of_files:
    # Path abstracts the underlying OS-specific path syntax 
    # Ex: \ for Windows and / for Unix-based systems
    # / for separator 
    # Cross-platform integration + Object Oriented 

    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath) # os.path.split("config/config.yaml") -> ("config", "config.yaml")

    # Create directory if not already exists
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    # Create file if not already exists
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass 
        logging.info(f"Creating empty file: {filepath}")
    
    else:
        logging.info(f"{filename} already exists")

print(os.path.getsize("README.md"))
