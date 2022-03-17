from sqlalchemy.orm import Session

from . import models, schemas

'''QUARTERLY CRUD'''

def get_weekly(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Weekly).offset(skip).limit(limit).all()

def get_moatq(db: Session, ticker: str):
    return db.query(models.Moatq).filter(models.Moatq.ticker == ticker).all()

def get_healthq(db: Session, ticker: str):
    return db.query(models.Healthq).filter(models.Healthq.ticker == ticker).all()

def get_financialsq(db: Session, ticker=str):
    return db.query(models.Financialsq).filter(models.Financialsq.ticker == ticker).all()

def get_growthq(db: Session, ticker=str):
    return db.query(models.Growthq).filter(models.Growthq.ticker == ticker).all()

'''YEARLY CRUD'''

def get_moaty(db: Session, ticker: str):
    return db.query(models.Moaty).filter(models.Moaty.ticker == ticker).all()

def get_healthy(db: Session, ticker: str):
    return db.query(models.Healthy).filter(models.Healthy.ticker == ticker).all()

def get_financialsy(db: Session, ticker=str):
    return db.query(models.Financialsy).filter(models.Financialsy.ticker == ticker).all()

def get_growthy(db: Session, ticker=str):
    return db.query(models.Growthy).filter(models.Growthy.ticker == ticker).all()
