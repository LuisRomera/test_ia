import yaml

def load_config(config_path):
    try:
        with open(config_path, 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        log.error(f"Configuration file not found: {config_path}")
        raise
    except yaml.YAMLError as e:
        log.error(f"Error parsing configuration file: {e}")
        raise
