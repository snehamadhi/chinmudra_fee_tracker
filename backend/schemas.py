from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    parent_phone: str
    batch: str
    upi_id: str
    password: str