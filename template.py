import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

list = [
    'src/mlproject/__init__.py',
    'src/mlproject/components/__init__.py',
    'src/mlproject/utils.py/__init__.py',
    'src/mlproject/utils.py/common.py',
    'src/project_name/config.py/__init__.py',
    'src/mlproject/config.py/configuration.py',
    'src/mlproject/pipeline/__init__.py',
    'src/mlproject/entity/__init__.py',
    'src/mlproject/entity/config_entity.py',
    'src/mlproject/constants__init__.py',
    'config/config.yaml',
    'params.yaml',
    'schema.yaml',
    'main.py',
    'app.py',
]

for filepath in list:
    filepath=Path(filepath)
    filedir, filename=os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'Creating directory: {filedir} for the file: {filename}')
    
    # Create the empty file
    if (not os.path.exists(filepath)):  
        with open(filepath, 'w'):
            pass
        logging.info(f"Created an empty file : {filename}")
    else: 
        logging.warning(f"File already exists: {filename}. Skipping...")
