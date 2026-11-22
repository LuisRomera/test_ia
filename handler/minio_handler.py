import os
from minio import Minio
from typing import Optional, List

log = logging.getLogger(__name__)

class MinIOHandler:
    def __init__(self, endpoint: str, access_key: str, secret_key: str, secure: bool):
        self.client = Minio(
            endpoint,
            access_key=access_key,
            secret_key=secret_key,
            secure=secure
        )

    def list_buckets(self) -> List[str]:
        buckets = self.client.list_buckets()
        return [bucket.name for bucket in buckets]

    def get_latest_file(self, bucket_name: str, prefix: Optional[str] = None) -> Optional[str]:
        objects = self.client.list_objects(bucket_name, prefix=prefix)
        latest_object = max(objects, key=lambda obj: obj.last_modified, default=None)
        return latest_object.object_name if latest_object else None
