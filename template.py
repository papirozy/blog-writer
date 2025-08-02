# A script to create Project structure
import os
from pathlib import Path
import logging


logging.basicConfig(level = logging.INFO, format = '[%(asctime)s]: %(message)s:')

list_of_files = [
    'requirements.txt',
    'backend/generate_blog.py',
    'app.py',
    '.env',
    'Dockerfile',
    'github/workflows/.gitkeep'
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok = True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")


