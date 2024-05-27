from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient

from data.config import *


class BaseDB:
    _instance = None

    def __init__(self):
        self.db = None
        self.collection = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = super(BaseDB, cls).__new__(cls)
        return cls._instance

    async def init_pool(self):
        try:
            if not isinstance(DB_NAME, str) or not isinstance(DB_COLLECTION, str):
                raise ValueError("DB_NAME and DB_COLLECTION must be strings.")

            client = AsyncIOMotorClient("mongodb://localhost:27017/")
            self.db = client[DB_NAME]
            self.collection = self.db[DB_COLLECTION]
        except Exception as e:
            print(f"Error initializing database: {e}")

    async def find(self):
        try:
            async for document in self.collection.find():
                yield document
        except Exception as e:
            print(f"Error fetching documents: {e}")


async def conn():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["MongoTest"]
    collection = db["sampleDB"]

    cursor = collection.find()
    return cursor
