#utils - functionality that is used frequently in your code
#say u want to read a .yaml file in every component. we can add it in the utils and import it in all components
#reusability of code

import os
from box.exceptions import BoxValueError
import yaml
from src.mlProject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    #reads yaml file and returns ConfigBox type
    #args path:str like input 
    #exceptions : 
    #raises valueError if the .yaml file is empty
    try:
        with open(path_to_yaml) as yaml_file:
           content = yaml.safe_load(yaml_file)
           logger.info(f"yaml file {path_to_yaml} loaded successfully")
           return ConfigBox(content)
    
    except BoxValueError:
        raise ValueError("Yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories:list, verbose=True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at {path}")


@ensure_annotations
def save_json(path:Path, data:dict):
    #save json data
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"file created at {path}")

@ensure_annotations
def load_json(path:Path) -> ConfigBox:
    #save json data
    with open(path) as f:
        content = json.load(f)
    logger.info(f"json file loaded successfully from {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data:Any, path:Path):
    #save binary file
    joblib.dump(value=data,filename=path)
    logger.info(f"binary file created at {path}")

@ensure_annotations
def load_bin(path:Path) -> Any:
    #load binary file
    data = joblib.load(path)
    logger.info(f"binary data loaded from {path}")
    return data

@ensure_annotations
def get_size(path:Path) -> str:
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"