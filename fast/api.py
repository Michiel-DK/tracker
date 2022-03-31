import uvicorn
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from jose import JWTError, jwt
from passlib.context import CryptContext
from typing import List
from sqlalchemy.orm import Session
from . import crud, schemas, authentification
from .database import SessionLocal
import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
SECRET_KEY = os.environ.get('SECRET_KEY')


fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    }
}

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


#tokenURL = url client will use to send username/password in order to get token 

app = FastAPI()

# def fake_hash_password(password: str):
#     return "fakehashed" + password

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

# @app.get("/weekly/", response_model=List[schemas.Weekly])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = crud.get_weekly(db, skip=skip, limit=limit)
#     return items

'''USERS ENDPOINTS'''

@app.get("/token/")
#will look in request for authorization header and check if value=Bearer + token => returns token as 'str'
def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}

@app.post("/token", response_model=schemas.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authentification.authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = authentification.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me")
def read_users_me(current_user: schemas.User = Depends(authentification.get_current_user)):
    return current_user

'''WEEKLY ENDPOINTS'''

@app.get("/prices/{ticker}", response_model=List[schemas.Prices])
def read_items(ticker: str, db: Session = Depends(get_db), current_user: schemas.User = Depends(authentification.get_current_user)):
    items = crud.get_prices(db, ticker=ticker)
    return items

@app.get("/weekly/{ticker}", response_model=List[schemas.Weekly])
def read_items(ticker: str, db: Session = Depends(get_db), current_user: schemas.User = Depends(authentification.get_current_user)):
    items = crud.get_weekly(db, ticker=ticker)
    return items

@app.get("/weekly_all/", response_model=List[schemas.Weekly])
def read_items(db: Session = Depends(get_db), current_user: schemas.User = Depends(authentification.get_current_user)):
    items = crud.get_all_tickers(db)
    return items
        
'''QUARTERLY ENDPOINTS'''

@app.get("/q_moat/{ticker}", response_model=List[schemas.Moatq])
def read_items(ticker: str, db: Session = Depends(get_db), current_user: schemas.User = Depends(authentification.get_current_user)):
    items = crud.get_moatq(db, ticker=ticker)
    return items

@app.get("/q_health/{ticker}", response_model=List[schemas.Healthq])
def read_items(ticker: str, db: Session = Depends(get_db), current_user: schemas.User = Depends(authentification.get_current_user)):
    items = crud.get_healthq(db, ticker=ticker)
    return items

@app.get("/q_financials/{ticker}", response_model=List[schemas.Financialsq])
def read_items(ticker: str, db: Session = Depends(get_db), current_user: schemas.User = Depends(authentification.get_current_user)):
    items = crud.get_financialsq(db, ticker=ticker)
    return items

@app.get("/q_growth/{ticker}", response_model=List[schemas.Growthq])
def read_items(ticker: str, db: Session = Depends(get_db), current_user: schemas.User = Depends(authentification.get_current_user)):
    items = crud.get_growthq(db, ticker=ticker)
    return items

'''YEARLY ENDPOINTS'''

@app.get("/y_moat/{ticker}", response_model=List[schemas.Moaty])
def read_items(ticker: str, db: Session = Depends(get_db), current_user: schemas.User = Depends(authentification.get_current_user)):
    items = crud.get_moaty(db, ticker=ticker)
    return items

@app.get("/y_health/{ticker}", response_model=List[schemas.Healthy])
def read_items(ticker: str, db: Session = Depends(get_db), current_user: schemas.User = Depends(authentification.get_current_user)):
    items = crud.get_healthy(db, ticker=ticker)
    return items

@app.get("/y_financials/{ticker}", response_model=List[schemas.Financialsy])
def read_items(ticker: str, db: Session = Depends(get_db), current_user: schemas.User = Depends(authentification.get_current_user)):
    items = crud.get_financialsy(db, ticker=ticker)
    return items

@app.get("/y_growth/{ticker}", response_model=List[schemas.Growthy])
def read_items(ticker: str, db: Session = Depends(get_db), current_user: schemas.User = Depends(authentification.get_current_user)):
    items = crud.get_growthy(db, ticker=ticker)
    return items

# @app.get("/weekly_info")
# async def get_weekly(ticker):
#     company_info, company_value, company_div, company_momentum, company_recom =  await asyncio.wait(get_weekly(ticker), return_when=asyncio.FIRST_COMPLETED)
#     return company_info[0]["ticker"][0]


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)