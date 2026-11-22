import os
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import logging

log = logging.getLogger(__name__)

class MongoHandler:
    def __init__(self, connection_string=None):
        if not connection_string:
            connection_string = os.getenv('MONGO_CONNECTION_STRING')
            if not connection_string:
                raise ValueError("MongoDB connection string is required")
        
        self.client = MongoClient(connection_string)
        log.info("Connected to MongoDB")

    def get_database(self, db_name):
        return self.client[db_name]

    def close_connection(self):
        self.client.close()
        log.info("Closed MongoDB connection")
