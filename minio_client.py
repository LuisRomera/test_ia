import os
import logging
from minio import Minio
from typing import List, Optional

log = logging.getLogger(__name__)

class MinioClient:
    def __init__(self):
        """
        Initializes the MinIO client using environment variables.
        Expected env vars:
        MINIO_ENDPOINT, MINIO_ACCESS_KEY, MINIO_SECRET_KEY, MINIO_SECURE (bool)
        """
        self.endpoint = os.getenv("MINIO_ENDPOINT", "localhost:9000")
        self.access_key = os.getenv("MINIO_ACCESS_KEY")
        self.secret_key = os.getenv("MINIO_SECRET_KEY")
        self.secure = os.getenv("MINIO_SECURE", "False").lower() == "true"

        if not self.access_key or not self.secret_key:
            log.error("MinIO credentials (MINIO_ACCESS_KEY, MINIO_SECRET_KEY) are missing.")
            raise ValueError("Missing MinIO credentials in environment variables.")

        try:
            self.client = Minio(
                self.endpoint,
                self.access_key,
                self.secret_key,
                secure=self.secure
            )
            log.info(f"Connected to MinIO at {self.endpoint}")
        except Exception as e:
            log.error(f"Failed to connect to MinIO: {e}")
            raise

    def list_buckets(self) -> List[str]:
        """Returns a list of bucket names."""
        try:
            buckets = self.client.list_buckets()
            return [bucket.name for bucket in buckets]
        except Exception as e:
            log.error(f"Error listing buckets: {e}")
            raise

    def upload_file(self, bucket_name: str, object_name: str, file_path: str):
        """Uploads a file to a specific bucket."""
        try:
            self.client.put_object(
                bucket_name, 
                object_name, 
                file_path, 
                length=os.path.getsize(file_path)
            )
            log.info(f"Successfully uploaded {object_name} to {bucket_name}")
        except Exception as e:
            log.error(f"Error uploading file: {e}")
            raise

if __name__ == "__main__":
    # Simple test if run directly
    client = MinioClient()
    print(client.list_buckets())
