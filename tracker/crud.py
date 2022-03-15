from sqlalchemy.orm import Session

from tracker import models, schemas

def get_weekly(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Weekly).offset(skip).limit(limit).all()

