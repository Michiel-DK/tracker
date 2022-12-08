from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, Date
from sqlalchemy.orm import relationship

from .database import Base

class Prices(Base):
    __tablename__ = "prices"

    index = Column(Integer, primary_key=False, index=True)
    date = Column(Date, primary_key=False, index=False)
    close = Column(Float, primary_key=False, index=False)
    ticker = Column(String, primary_key=False, index=False)
    key = Column(String, unique=True, primary_key=True, index=False)

'''Weekly models'''

class Weekly(Base):
    __tablename__ = "weekly_info"
    #id columns
    index = Column(Integer, primary_key=False, index=True)
    ticker = Column(String, primary_key=False, index=False)
    key = Column(String, unique=True, primary_key=True, index=False)
    date = Column(Date, primary_key=False, index=False)
    
    #general columns
    bookvalue = Column(Float, primary_key=False, index=False)
    country = Column(String, primary_key=False, index=False)
    currency = Column(String, primary_key=False, index=False)
    currentprice: Column(Float, primary_key=False, index=False)
    enterprisevalue = Column(Integer, primary_key=False, index=True)
    exchange = Column(String, primary_key=False, index=False)
    fulltimeemployees = Column(Integer, primary_key=False, index=True)
    sector = Column(String, primary_key=False, index=False)
    industry = Column(String, primary_key=False, index=False)
    isesgpopulated = Column(Boolean, primary_key=False, index=False)
    longbusinesssummary = Column(String, primary_key=False, index=False)
    longname = Column(String, primary_key=False, index=False)
    market = Column(String, primary_key=False, index=False)
    marketcap = Column(Integer, primary_key=False, index=False)
    beta : Column(Float, primary_key=False, index=False)
    beta3year = Column(String, primary_key=False, index=False)
    
    #analyst columns
    recommendationmean = Column(Float, primary_key=False, index=False)
    recommendationkey = Column(String, primary_key=False, index=False)
    morningstaroverallrating = Column(String, primary_key=False, index=False)
    morningstarriskrating = Column(String, primary_key=False, index=False)
    numberofanalystopinions = Column(Integer, primary_key=False, index=True)
    sharesshort = Column(Integer, primary_key=False, index=True)
    shortratio = Column(Float, primary_key=False, index=False)
    targetlowprice = Column(Float, primary_key=False, index=False)
    targethighprice = Column(Float, primary_key=False, index=False)
    targetmedianprice = Column(Float, primary_key=False, index=False)
    targetmeanprice = Column(Float, primary_key=False, index=False)
    
    #value columns
    currentratio = Column(Float, primary_key=False, index=False)
    debttoequity = Column(Float, primary_key=False, index=False)
    enterprisetoebitda = Column(Float, primary_key=False, index=False)
    enterprisetorevenue = Column(Float, primary_key=False, index=False)
    forwardpe = Column(Float, primary_key=False, index=False)
    trailingpe = Column(Float, primary_key=False, index=False)
    pricetosalestrailing12months = Column(Float, primary_key=False, index=False)
    pricetobook = Column(Float, primary_key=False, index=False)
    quickratio = Column(Float, primary_key=False, index=False)
    
    #dividend columns
    dividendrate = Column(Float, primary_key=False, index=False)
    dividendyield = Column(Float, primary_key=False, index=False)
    fiveyearavgdividendyield = Column(Float, primary_key=False, index=False)
    exdividenddate = Column(Integer, primary_key=False, index=True)
    payoutratio = Column(Float, primary_key=False, index=False)
    
    #growth columns
    earningsgrowth = Column(Float, primary_key=False, index=False)
    earningsquarterlygrowth = Column(Float, primary_key=False, index=False)
    revenuegrowth = Column(Float, primary_key=False, index=False)
    revenuequarterlygrowth = Column(String, primary_key=False, index=False)
    freecashflow = Column(Integer, primary_key=False, index=True)
    
    #profitability columns
    ebitdamargins = Column(Float, primary_key=False, index=False)
    grossmargins = Column(Float, primary_key=False, index=False)
    returnonassets = Column(Float, primary_key=False, index=False)
    returnonequity = Column(Float, primary_key=False, index=False)
    profitmargins = Column(Float, primary_key=False, index=False)
    
    #price columns
    currentprice = Column(Float, primary_key=False, index=False)
    fiftydayaverage = Column(Float, primary_key=False, index=False)
    fiftytwoweeklow = Column(Float, primary_key=False, index=False)
    fiftytwoweekhigh = Column(Float, primary_key=False, index=False)
    twohundreddayaverage = Column(Float, primary_key=False, index=False)
    
    #momentum columns
    fiveyearaveragereturn = Column(String, primary_key=False, index=False)
    threeyearaveragereturn = Column(String, primary_key=False, index=False)
    
    #earnings columns
    forwardeps = Column(Float, primary_key=False, index=False)
    trailingeps = Column(Float, primary_key=False, index=False)
    
    #ownership columns
    heldpercentinsiders = Column(Float, primary_key=False, index=False)
    heldpercentinstitutions = Column(Float, primary_key=False, index=False)
    impliedsharesoutstanding = Column(String, primary_key=False, index=False)
    floatshares = Column(Integer, primary_key=False, index=True)
    sharesoutstanding = Column(Integer, primary_key=False, index=True)
    
    #balance columms
    totalassets = Column(String, primary_key=False, index=True)
    totalcash = Column(Integer, primary_key=False, index=True)
    totalcashpershare = Column(Float, primary_key=False, index=False)
    totaldebt = Column(Integer, primary_key=False, index=True)
    totalrevenue = Column(Integer, primary_key=False, index=True)
    grossprofits = Column(Integer, primary_key=False, index=True)
    operatingcashflow = Column(Integer, primary_key=False, index=True)

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
    
