import os
from fastapi import APIRouter, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from models.finances import Finance
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()
templates = Jinja2Templates(directory='templates')

# GET index.html
@router.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html",{"request":request})

@router.get('/favicon.ico')
async def favicon():
    return FileResponse("./static/favicon.ico")

# GET Request Method
@router.get("/finances")
async def get_finances():
    finances = list_serial(collection_name.find())
    return finances

# POST Request Method
@router.post("/finances")
async def post_finance(finance: Finance):
    collection_name.insert_one(dict(finance))
    
@router.get("/easteregg")
async def easteregg():
    return "https://blog.winterflw.com"