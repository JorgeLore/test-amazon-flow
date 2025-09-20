from pydantic import BaseModel, EmailStr

class PurchaseRequest(BaseModel):
    email: EmailStr
    password: str
    headless: bool=False