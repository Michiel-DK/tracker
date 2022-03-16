from sqlalchemy.orm import Session

from tracker import models, schemas

def get_weekly(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Weekly).offset(skip).limit(limit).all()

def get_moatq(db: Session, ticker: str):
    return db.query(models.Moatq).filter(models.Moatq.ticker == ticker).all()

def get_healthq(db: Session, ticker: str):
    return db.query(models.Healthq).filter(models.Healthq.ticker == ticker).all()

def get_financialsq(db: Session, ticker=str):
    return db.query(models.Financialsq).filter(models.Financialsq.ticker == ticker).all()