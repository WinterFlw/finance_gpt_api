from pymongo import MongoClien
from ..api_key import get_key

client = MongoClien(get_key("MONGO_URI"))

db = client.finance_db

collection_name = db["finance_collection"]