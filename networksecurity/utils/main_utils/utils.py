import yaml
from networksecurity.exception.exception import NetwokSecurityException
from networksecurity.logging.logger import logging
import os, sys
import numpy as np
#import dill
import pickle

def read_yaml_file(file_path : str) -> dict:
    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise NetwokSecurityException(e, sys)

def write_ymal_file(
        file_path: str,
        content: object,
        replace: bool = False
) -> None:
    try:
        if replace and os.path.exists(file_path):
            os.remove(file_path)

        os.makedirs(
            os.path.dirname(file_path),
            exist_ok=True
        )

        with open(file_path, "w") as file:
            yaml.dump(content, file)

    except Exception as e:
        raise NetwokSecurityException(e, sys)