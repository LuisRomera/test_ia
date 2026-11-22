import logging
from typing import Optional, List
from minio import Minio
from minio.error import S3Error
from datetime import datetime

log = logging.getLogger(__name__)

class MinioClient:
    """Client to interact with a MinIO (S3-compatible) storage service."""

    def __init__(self, endpoint: str, access_key: str, secret_key: str, secure: bool = False):
        """Initializes the MinIO client."""
        try:
            self.client = Minio(
                endpoint=endpoint,
                access_key=access_key,
                secret_key=secret_key,
                secure=secure
            )
            log.info(f"MinIO client initialized for endpoint: {endpoint}")
        except Exception as e:
            log.error(f"Failed to initialize MinIO client: {e}")
            raise

    def list_buckets(self) -> list:
        """Lists all available buckets."""
        try:
            buckets = self.client.list_buckets()
            return [bucket.name for bucket in buckets]
        except S3Error as e:
            log.error(f"Error listing buckets: {e}")
            raise

    def upload_file(self, bucket_name: str, object_name: str, file_path: str) -> bool:
        """Uploads a file to the specified bucket."""
        try:
            self.client.put_object(
                bucket_name,
                object_name,
                file_path,
                length=None, # Minio handles length if it's a file path
                content_type="application/octet-stream"
            )
            log.info(f"Successfully uploaded {object_name} to {bucket_name}")
            return True
        except S3Error as e:
            log.error(f"Error uploading file {object_name}: {e}")
            raise

    def get_latest_file(self, bucket_name: str, prefix: str) -> Optional[str]:
        """
        Retrieves the name of the most recently modified file in a given path (prefix).
        
        Args:
            bucket_name: The name of the bucket.
            prefix: The path/prefix to search within.
            
        Returns:
            The name of the latest object or None if none found.
        """
        try:
            objects = self.client.list_objects(bucket_name, prefix=prefix, recursive=True)
            
            latest_file = None
            latest_date = datetime.min

            for obj in objects:
                if obj.last_modified > latest_date:
                    latest_date = obj.last_modified
                    latest_file = obj.object_name

            log.info(f"Latest file found in {prefix}: {latest_file}")
            return latest_file
        except S3Error as e:
            log.error(f"Error retrieving latest file from {prefix}: {e}")
            raise

if __name__ == "__main__":
    # Example usage (would normally be driven by config)
    try:
        client = MinioClient("localhost:9000", "minioadmin", "minioadmin")
        print(f"Buckets: {client.list_buckets()}")
        # Example call:
        # client.get_latest_file("my-bucket", "data/logs/")
    except Exception as e:
        print(f"Test failed: {e}")
