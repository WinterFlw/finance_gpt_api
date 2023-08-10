from fastapi import APIRouter, Form, Request
from fastapi.templating import Jinja2Templates
from models.finances import Finance
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId

templates = Jinja2Templates(directory='templates')
router = APIRouter()
# GET index.html
@router.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html",{"request":request})

# GET Request Method
@router.get("/finances")
async def get_finances():
    finances = list_serial(collection_name.find())
    return finances

# POST Request Method
@router.post("/finances")
async def post_finance(finance: Finance):
    collection_name.insert_one(dict(finance))