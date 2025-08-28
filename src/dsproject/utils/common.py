import os
import yaml
from src.dsproject import logger
import json
import joblib #for pickle file
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path line input
    
    Raises:
        ValueError: if yaml file empty
        e: empty file

    Returns:
        Configbox: Configbox type

    """
    