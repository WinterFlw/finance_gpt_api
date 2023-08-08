from pydantic import BaseModel

#구현중
class finance(BaseModel):
    stock: str
    price: int
    news: str
