from fastapi import APIRouter
from models.finances import Finance
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObrectId

router = APIRouter()

# GET Request Method
async def get_finances():
    finances = list_serial(collection_name.find())
    return finances