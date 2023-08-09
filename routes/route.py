from fastapi import APIRouter
from models.finances import Finance
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()

# GET Request Method
@router.get("/")
async def get_finances():
    finances = list_serial(collection_name.find())
    return finances

# POST Request Method
@router.post("/")
async def post_finance(finance: Finance):
    collection_name.insert_one(dict(finance))