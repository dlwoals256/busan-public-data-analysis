from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.api.database import SessionLocal
from src.api import models, schemas

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/chargers', response_model=list[schemas.EVChargerResponse])
def get_chargers(
    skip:int=0,
    limit:int=100,
    db:Session=Depends(get_db)
):
    chargers = db.query(models.EVCharger).offset(skip).limit(limit).all()
    return chargers

