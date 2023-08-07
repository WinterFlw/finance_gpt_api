from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
import api_key
app = FastAPI()

from pymongo.mongo_client import MongoClient

uri = api_key.get_key("MONGO_URI")

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