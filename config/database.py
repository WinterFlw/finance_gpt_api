from pymongo import MongoClient
from api_key import get_key
uri = get_key("MONGO_URI")
client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    print(uri)
except Exception as e:
    print(e)
    
db = client.finance_db

collection_name = db["finance_collection"]