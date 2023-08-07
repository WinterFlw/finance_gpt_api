from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from app.api_key import get_key
app = FastAPI()

from pymongo.mongo_client import MongoClient

uri = get_key("MONGO_URI")
print(uri)
# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

"""
@app.get("/")
async def root():
    return {"message": "Hello World"}
"""

#uvicorn app.main:app --reload --host=0.0.0.0 --port=80