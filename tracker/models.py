from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from tracker.database import Base

class Weekly(Base):
    __tablename__ = "weekly_info"

    index = Column(Integer, primary_key=False, index=True)
    ticker = Column(String, primary_key=False, index=False)
    grossmargins = Column(Float, primary_key=False, index=False)
    key = Column(String, unique=True, primary_key=True, index=False)

    #items = relationship("Item", back_populates="owner")