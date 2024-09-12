from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from . import models, schemas

'''OTHER CRUD'''
def get_weekly(db: Session, ticker:str):
    return db.query(models.Weekly).filter(models.Weekly.ticker == ticker).all()

def get_all_tickers(db: Session):
    return db.query(models.Weekly).distinct()

def get_prices(db: Session, ticker:str):
    return db.query(models.Prices).filter(models.Prices.ticker == ticker).all()

def get_random_weekly(db: Session):
    return db.query(models.Weekly).order_by(func.random()).first()

'''QUARTERLY CRUD'''

def get_moatq(db: Session, ticker: str):
    return db.query(models.Moatq).filter(models.Moatq.ticker == ticker).all()

def get_healthq(db: Session, ticker: str):
    return db.query(models.Healthq).filter(models.Healthq.ticker == ticker).all()

def get_financialsq(db: Session, ticker=str):
    return db.query(models.Financialsq).filter(models.Financialsq.ticker == ticker).all()

def get_financialsq_target(db: Session, year=str):
    return db.query(models.Financialsq).filter(models.Financialsq.year != year).all()

def get_financialsq_current(db: Session, year=str):
    return db.query(models.Financialsq).filter(models.Financialsq.year == year).all()

def get_growthq(db: Session, ticker=str):
    return db.query(models.Growthq).filter(models.Growthq.ticker == ticker).all()

def get_oldest_q(db: Session):
    return db.query(models.Financialsq).order_by(models.Financialsq.date.asc()).first()

'''YEARLY CRUD'''

def get_moaty(db: Session, ticker: str):
    return db.query(models.Moaty).filter(models.Moaty.ticker == ticker).all()

def get_healthy(db: Session, ticker: str):
    return db.query(models.Healthy).filter(models.Healthy.ticker == ticker).all()

def get_financialsy(db: Session, ticker=str):
    return db.query(models.Financialsy).filter(models.Financialsy.ticker == ticker).all()

def get_growthy(db: Session, ticker=str):
    return db.query(models.Growthy).filter(models.Growthy.ticker == ticker).all()
