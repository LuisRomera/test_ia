import logging
import os
import yaml
from typing import Any, Dict

log = logging.getLogger(__name__)

class ConfigLoader:
    """Class to handle loading and accessing configuration from a YAML file."""

    def __init__(self, config_path: str):
        self.config_path = config_path
        self._config: Dict[str, Any] = {}
        self.load()

    def load(self) -> None:
        """Loads the YAML configuration into a dictionary."""
        if not os.path.exists(self.config_path):
            log.error(f"Configuration file not found at {self.config_path}")
            raise FileNotFoundError(f"Config file missing: {self.config_path}")

        try:
            with open(self.config_path, 'r') as f:
                data = yaml.safe_load(f)
                self._config = data if data is not None else {}
            log.info("Configuration loaded successfully.")
        except yaml.YAMLError as e:
            log.error(f"Error parsing YAML file: {e}")
            raise

    def get(self, key: str, default: Any = None) -> Any:
        """Returns a value from the config dictionary or a default value."""
        return self._config.get(key, default)

    @property
    def all_config(self) -> Dict[str, Any]:
        """Returns the entire configuration as a dictionary."""
        return self._config
