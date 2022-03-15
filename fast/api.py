import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
#from tracker.frontend_functions import *
import asyncio

from typing import List

from sqlalchemy.orm import Session

from tracker import crud, models, schemas
from tracker.database import SessionLocal, engine
    

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/weekly/", response_model=List[schemas.Weekly])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_weekly(db, skip=skip, limit=limit)
    return items

# @app.get("/weekly_info")
# async def get_weekly(ticker):
#     company_info, company_value, company_div, company_momentum, company_recom =  await asyncio.wait(get_weekly(ticker), return_when=asyncio.FIRST_COMPLETED)
#     return company_info[0]["ticker"][0]


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)