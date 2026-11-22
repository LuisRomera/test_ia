#!/usr/bin/env python3

import logging
import yaml
import os
from typing import Any, Dict

log = logging.getLogger(__name__)

def load_config(config_path: str) -> Dict[str, Any]:
    """Loads the YAML configuration file into a dictionary."""
    if not os.path.exists(config_path):
        log.error(f"Configuration file not found at {config_path}")
        raise FileNotFoundError(f"Config file missing: {config_path}")
    
    with open(config_path, 'r') as f:
        return yaml.safe_load(f) or {}

def greet(name: str):
    log.info(f'Hello, {name}!')

if __name__ == '__main__':
    config_path = os.path.join('resources', 'config.yaml')
    try:
        config = load_config(config_path)
        # Example of accessing the dictionary values
        db_url = config.get('database_url', 'No URL provided')
        log.info(f"Loaded configuration. Database URL: {db_url}")
        
        greet('World')
    except Exception as e:
        log.exception("Failed to initialize the job")
        exit(1)
