from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    parent_phone = Column(String, unique=True, nullable=False)
    batch = Column(String, nullable=False)
    upi_id = Column(String, nullable=False)
    status = Column(String, default="pending")
