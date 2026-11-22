import argparse
import sys  # Added to fix 'sys' is not defined error
from config_loader import load_config
from handler.minio_handler import MinIOHandler
from handler.mongo_handler import MongoHandler
import logging

log = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Process some files.")
    parser.add_argument('--mongo-connection-string', type=str, help='MongoDB connection string')
    args = parser.parse_args()

    try:
        config = load_config('resources/config.yaml')
        minio_handler = MinIOHandler(config['minio'])
        mongo_handler = MongoHandler(args.mongo_connection_string)

        # Example usage
        db = mongo_handler.get_database('example_db')
        log.info("Database selected: example_db")

    except Exception as e:
        log.exception("An error occurred")
        sys.exit(1)

if __name__ == "__main__":
    main()
