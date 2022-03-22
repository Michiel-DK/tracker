from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from .database import Base

class Prices(Base):
    __tablename__ = "prices"

    index = Column(Integer, primary_key=False, index=True)
    date = Column(String, primary_key=False, index=False)
    close = Column(Float, primary_key=False, index=False)
    ticker = Column(String, primary_key=False, index=False)
    key = Column(String, unique=True, primary_key=True, index=False)

'''Weekly models'''

class Weekly(Base):
    __tablename__ = "weekly_info"

    index = Column(Integer, primary_key=False, index=True)
    ticker = Column(String, primary_key=False, index=False)
    grossmargins = Column(Float, primary_key=False, index=False)
    key = Column(String, unique=True, primary_key=True, index=False)

    #items = relationship("Item", back_populates="owner")
    
'''QUARTERLY models'''
    
class Moatq(Base):
    __tablename__ = "quarterly_moat"
    
    index = Column(Integer, primary_key=False, index=True)
    operatingmargin = Column(Float, primary_key=False, index=False)
    fcfmargin = Column(Float, primary_key=False, index=False)
    roa = Column(Float, primary_key=False, index=False)
    roe = Column(Float, primary_key=False, index=False)
    moatpercentage = Column(Float, primary_key=False, index=False)
    year = Column(String, primary_key=False, index=False)
    ticker = Column(String, primary_key=False, index=False)
    key = Column(String, unique=True, primary_key=True, index=False)
    
class Healthq(Base):
    __tablename__ = "quarterly_health"
    
    index = Column(Integer, primary_key=False, index=True)
    receivablessales = Column(Float, primary_key=False, index=False)
    currentratio = Column(Float, primary_key=False, index=False)
    financialleverage = Column(Float, primary_key=False, index=False)
    debtequity = Column(Float, primary_key=False, index=False)
    percentage = Column(Float, primary_key=False, index=False)
    year = Column(String, primary_key=False, index=False)
    ticker = Column(String, primary_key=False, index=False)
    key = Column(String, unique=True, primary_key=True, index=False)
    
class Financialsq(Base):
    __tablename__ = "quarterly_financials"
    
    index = Column(Integer, primary_key=False, index=True)
    assetturnover = Column(Float, primary_key=False, index=False)
    cashdebt = Column(Float, primary_key=False, index=False)
    currentratio = Column(Float, primary_key=False, index=False)
    debtequity = Column(Float, primary_key=False, index=False)
    equitymultipl = Column(Float, primary_key=False, index=False)
    fcfmargin = Column(Integer, primary_key=False, index=True)
    financialleverage = Column(Float, primary_key=False, index=False)
    goodwillassets = Column(Float, primary_key=False, index=False)
    netmargin = Column(Float, primary_key=False, index=False)
    operatingmargin = Column(Float, primary_key=False, index=False)
    receivablessales = Column(Float, primary_key=False, index=False)
    roa = Column(Float, primary_key=False, index=False)
    roe = Column(Float, primary_key=False, index=False)
    roic = Column(Float, primary_key=False, index=False)
    year = Column(String, primary_key=False, index=False)
    ticker = Column(String, primary_key=False, index=False)
    key = Column(String, unique=True, primary_key=True, index=False)
    
class Growthq(Base):
    __tablename__ = "quarterly_growth"
    
    index = Column(Integer, primary_key=False, index=True)
    capitalexpenditures = Column(Float, primary_key=False, index=False)
    cash = Column(Float, primary_key=False, index=False)
    fcf = Column(Float, primary_key=False, index=False)
    goodwill = Column(Float, primary_key=False, index=False)
    netincome = Column(Float, primary_key=False, index=False)
    revenue = Column(Integer, primary_key=False, index=True)
    longtermdebt = Column(Float, primary_key=False, index=False)
    assetturnover = Column(Float, primary_key=False, index=False)
    fcfmargin = Column(Float, primary_key=False, index=False)
    netmargin = Column(Float, primary_key=False, index=False)
    operatingmargin = Column(Float, primary_key=False, index=False)
    roa = Column(Float, primary_key=False, index=False)
    roe = Column(Float, primary_key=False, index=False)
    roic = Column(Float, primary_key=False, index=False)
    currentratio = Column(Float, primary_key=False, index=False)
    financialleverage = Column(Float, primary_key=False, index=False)
    receivablessales = Column(Float, primary_key=False, index=False)
    debtequity = Column(Float, primary_key=False, index=False)
    equityasset = Column(Float, primary_key=False, index=False)
    goodwillassets = Column(Float, primary_key=False, index=False)
    year = Column(String, primary_key=False, index=False)
    ticker = Column(String, primary_key=False, index=False)
    key = Column(String, unique=True, primary_key=True, index=False)
    
'''YEARLY models'''
    
class Moaty(Base):
    __tablename__ = "yearly_moat"
    
    index = Column(Integer, primary_key=False, index=True)
    operatingmargin = Column(Float, primary_key=False, index=False)
    fcfmargin = Column(Float, primary_key=False, index=False)
    roa = Column(Float, primary_key=False, index=False)
    roe = Column(Float, primary_key=False, index=False)
    moatpercentage = Column(Float, primary_key=False, index=False)
    year = Column(String, primary_key=False, index=False)
    ticker = Column(String, primary_key=False, index=False)
    key = Column(String, unique=True, primary_key=True, index=False)
    
class Healthy(Base):
    __tablename__ = "yearly_health"
    
    index = Column(Integer, primary_key=False, index=True)
    receivablessales = Column(Float, primary_key=False, index=False)
    currentratio = Column(Float, primary_key=False, index=False)
    financialleverage = Column(Float, primary_key=False, index=False)
    debtequity = Column(Float, primary_key=False, index=False)
    percentage = Column(Float, primary_key=False, index=False)
    year = Column(String, primary_key=False, index=False)
    ticker = Column(String, primary_key=False, index=False)
    key = Column(String, unique=True, primary_key=True, index=False)
    
class Financialsy(Base):
    __tablename__ = "yearly_financials"
    
    index = Column(Integer, primary_key=False, index=True)
    assetturnover = Column(Float, primary_key=False, index=False)
    cashdebt = Column(Float, primary_key=False, index=False)
    currentratio = Column(Float, primary_key=False, index=False)
    debtequity = Column(Float, primary_key=False, index=False)
    equitymultipl = Column(Float, primary_key=False, index=False)
    fcfmargin = Column(Integer, primary_key=False, index=True)
    financialleverage = Column(Float, primary_key=False, index=False)
    goodwillassets = Column(Float, primary_key=False, index=False)
    netmargin = Column(Float, primary_key=False, index=False)
    operatingmargin = Column(Float, primary_key=False, index=False)
    receivablessales = Column(Float, primary_key=False, index=False)
    roa = Column(Float, primary_key=False, index=False)
    roe = Column(Float, primary_key=False, index=False)
    roic = Column(Float, primary_key=False, index=False)
    year = Column(String, primary_key=False, index=False)
    ticker = Column(String, primary_key=False, index=False)
    key = Column(String, unique=True, primary_key=True, index=False)
    
class Growthy(Base):
    __tablename__ = "yearly_growth"
    
    index = Column(Integer, primary_key=False, index=True)
    capitalexpenditures = Column(Float, primary_key=False, index=False)
    cash = Column(Float, primary_key=False, index=False)
    fcf = Column(Float, primary_key=False, index=False)
    goodwill = Column(Float, primary_key=False, index=False)
    netincome = Column(Float, primary_key=False, index=False)
    revenue = Column(Integer, primary_key=False, index=True)
    longtermdebt = Column(Float, primary_key=False, index=False)
    assetturnover = Column(Float, primary_key=False, index=False)
    fcfmargin = Column(Float, primary_key=False, index=False)
    netmargin = Column(Float, primary_key=False, index=False)
    operatingmargin = Column(Float, primary_key=False, index=False)
    roa = Column(Float, primary_key=False, index=False)
    roe = Column(Float, primary_key=False, index=False)
    roic = Column(Float, primary_key=False, index=False)
    currentratio = Column(Float, primary_key=False, index=False)
    financialleverage = Column(Float, primary_key=False, index=False)
    receivablessales = Column(Float, primary_key=False, index=False)
    debtequity = Column(Float, primary_key=False, index=False)
    equityasset = Column(Float, primary_key=False, index=False)
    goodwillassets = Column(Float, primary_key=False, index=False)
    year = Column(String, primary_key=False, index=False)
    ticker = Column(String, primary_key=False, index=False)
    key = Column(String, unique=True, primary_key=True, index=False)
    
