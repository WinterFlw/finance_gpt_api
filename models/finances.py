from pydantic import BaseModel

#구현중
class Finance(BaseModel):
    stock: str
    price: str
    news: str
