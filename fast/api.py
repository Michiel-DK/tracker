import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
#from tracker.frontend_functions import *
import asyncio

from typing import List

from sqlalchemy.orm import Session

from tracker.db import crud, models, schemas
from tracker.db.database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware
    
    
    

app = FastAPI()

app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

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
        
'''QUARTERLY ENDPOINTS'''

@app.get("/q_moat/{ticker}", response_model=List[schemas.Moatq])
def read_items(ticker: str, db: Session = Depends(get_db)):
    items = crud.get_moatq(db, ticker=ticker)
    return items

@app.get("/q_health/{ticker}", response_model=List[schemas.Healthq])
def read_items(ticker: str, db: Session = Depends(get_db)):
    items = crud.get_healthq(db, ticker=ticker)
    return items

@app.get("/q_financials/{ticker}", response_model=List[schemas.Financialsq])
def read_items(ticker: str, db: Session = Depends(get_db)):
    items = crud.get_financialsq(db, ticker=ticker)
    return items

@app.get("/q_growth/{ticker}", response_model=List[schemas.Growthq])
def read_items(ticker: str, db: Session = Depends(get_db)):
    items = crud.get_growthq(db, ticker=ticker)
    return items

'''YEARLY ENDPOINTS'''

@app.get("/y_moat/{ticker}", response_model=List[schemas.Moaty])
def read_items(ticker: str, db: Session = Depends(get_db)):
    items = crud.get_moaty(db, ticker=ticker)
    return items

@app.get("/y_health/{ticker}", response_model=List[schemas.Healthy])
def read_items(ticker: str, db: Session = Depends(get_db)):
    items = crud.get_healthy(db, ticker=ticker)
    return items

@app.get("/y_financials/{ticker}", response_model=List[schemas.Financialsy])
def read_items(ticker: str, db: Session = Depends(get_db)):
    items = crud.get_financialsy(db, ticker=ticker)
    return items

@app.get("/y_growth/{ticker}", response_model=List[schemas.Growthy])
def read_items(ticker: str, db: Session = Depends(get_db)):
    items = crud.get_growthy(db, ticker=ticker)
    return items

# @app.get("/weekly_info")
# async def get_weekly(ticker):
#     company_info, company_value, company_div, company_momentum, company_recom =  await asyncio.wait(get_weekly(ticker), return_when=asyncio.FIRST_COMPLETED)
#     return company_info[0]["ticker"][0]


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)