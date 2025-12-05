from fastapi import FastAPI
from database import Base, engine
import models   # ← ADD THIS
from fastapi import Depends
from sqlalchemy.orm import Session
from deps import get_db
from schemas import UserCreate
from models import User

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello from backend!"}

@app.post("/signup")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(
        name=user.name,
        parent_phone=user.parent_phone,
        batch=user.batch,
        upi_id=user.upi_id,
        status="pending"
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "Signup request submitted", "user_id": new_user.id}
Base.metadata.create_all(bind=engine)
