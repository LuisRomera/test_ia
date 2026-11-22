#!/usr/bin/env python3

import logging
import os
from typing import Any

from config_loader import ConfigLoader

log = logging.getLogger(__name__)

def greet(name: str):
    log.info(f'Hello, {name}!')

if __name__ == '__main__':
    config_path = os.path.join('resources', 'config.yaml')
    try:
        # Use the ConfigLoader class to handle YAML reading
        loader = ConfigLoader(config_path)
        
        # Accessing values as a dictionary via the loader
        db_url = loader.get('database_url', 'No URL provided')
        log.info(f"Loaded configuration. Database URL: {db_url}")

        # Initialize MinIO Client using config
        minio_cfg = loader.get('minio')
        if minio_cfg:
            from minio_client import MinioClient
            m_client = MinioClient(
                endpoint=minio_cfg['endpoint'],
                access_key=minio_cfg['access_key'],
                secret_key=minio_cfg['secret_key']
            )
            log.info(f"MinIO Buckets: {m_client.list_buckets()}")

        greet('World')
    except Exception as e:
        log.exception("Failed to initialize the job")
        exit(1)
