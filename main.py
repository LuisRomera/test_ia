import argparse
import logging
from config_loader import load_config
from handler.minio_handler import MinIOHandler

log = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Interact with MinIO to retrieve file metadata.")
    args = parser.parse_args()

    try:
        config = load_config("resources/config.yaml")
        minio_client = MinIOHandler(
            endpoint=config['minio']['endpoint'],
            access_key=os.getenv('MINIO_ACCESS_KEY', config['minio']['access_key']),
            secret_key=os.getenv('MINIO_SECRET_KEY', config['minio']['secret_key']),
            secure=config['minio']['secure']
        )

        buckets = minio_client.list_buckets()
        log.info(f"Available buckets: {buckets}")

        latest_file = minio_client.get_latest_file(config['minio']['bucket'], prefix=config['minio'].get('prefix', ''))
        if latest_file:
            log.info(f"Latest file in bucket '{config['minio']['bucket']}': {latest_file}")
        else:
            log.warning("No files found in the specified bucket.")

    except Exception as e:
        log.exception("An error occurred while interacting with MinIO.")
        sys.exit(1)

if __name__ == "__main__":
    main()
