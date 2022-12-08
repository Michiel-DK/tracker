from typing import List, Optional, Union
import datetime
from pydantic import BaseModel

'''OTHER Pydantic models / schemas '''

class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

class UserInDB(User):
    hashed_password: str
    
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

'''WEEKLY Pydantic models / schemas '''
class PricesBase(BaseModel):
    date: datetime.date
    close: Optional[float] = None
    ticker: str
    key: str
    
class PricesCreate(PricesBase):
    pass

class Weekly_Id(BaseModel):
    """Id subclass for weekly api call"""
    ticker: str
    key: str
    date: datetime.date
    
class Weekly_General(BaseModel):
    '''General subclass for weekly api call'''
    bookvalue: Optional[float] = None
    country: Optional[str] = None
    currency: Optional[str] = None
    currentprice: Optional[float] = None
    enterprisevalue : Optional[int] = None
    exchange : Optional[str] = None
    fulltimeemployees : Optional[int] = None
    sector: Optional[str] = None
    industry: Optional[str] = None
    isesgpopulated: Optional[bool] = None
    longbusinesssumary: Optional[str] = None
    longname: Optional[str] = None
    market : Optional[str] = None
    marketcap: Optional[int] = None
    beta : Optional[float] = None
    beta3year : Optional[str] = None
    
class Weekly_Analysts(BaseModel):
    '''Analyst subclass for weekly api call'''
    recommendationmean: Optional[float] = None
    recommendationkey: Optional[str] = None
    morningstaroverallrating: Optional[str] = None
    morningstarriskrating: Optional[str] = None
    numberofanalystopinions: Optional[int] = None
    sharesshort: Optional[int] = None
    shortratio: Optional[float] = None
    targetlowprice: Optional[float] = None
    targethighprice: Optional[float] = None
    targetmedianprice: Optional[float] = None
    targetmeanprice: Optional[float] = None
    
class Weekly_Value(BaseModel):
    '''Value subclass for weekly api call'''
    currentratio: Optional[float] = None
    debttoequity: Optional[float] = None
    enterprisetoebitda: Optional[float] = None
    enterprisetorevenue: Optional[float] = None
    forwardpe: Optional[float] = None
    trailingpe: Optional[float] = None
    pricetosalestrailing12months: Optional[float] = None
    pricetobook: Optional[float] = None
    quickratio: Optional[float] = None
    
class Weekly_Dividend(BaseModel):
    '''Dividend subclass for weekly api call'''
    dividendrate: Optional[float] = None
    dividendyield: Optional[float] = None
    fiveyearavgdividendyield: Optional[float] = None
    exdividenddate: Optional[int] = None
    payoutratio: Optional[float] = None
    
class Weekly_Growth(BaseModel):
    ''' Growth subclass for weekly api call'''
    earningsgrowth: Optional[float] = None
    earningsquarterlygrowth: Optional[float] = None
    revenuegrowth: Optional[float] = None
    revenuequarterlygrowth: Optional[str] = None
    freecashflow: Optional[int] = None
    
class Weekly_Profitability(BaseModel):
    ''' Profitability subclass for weekly api call'''
    ebitdamargins: Optional[float] = None
    grossmargins: Optional[float] = None
    returnonassets: Optional[float] = None
    returnonequity: Optional[float] = None
    profitmargins: Optional[float] = None
    
class Weekly_Price(BaseModel):
    '''Price subclass for weekly api call'''
    currentprice: Optional[float] = None
    fiftydayaverage: Optional[float] = None
    fiftytwoweeklow: Optional[float] = None
    fiftytwoweekhigh: Optional[float] = None
    twohundreddayaverage: Optional[float] = None
    
class Weekly_Momentum(BaseModel):
    '''Momentum subclass for weekly api call'''
    fiveyearaveragereturn: Optional[str] = None
    threeyearaveragereturn: Optional[str] = None
    
class Weekly_Earnings(BaseModel):
    '''Earnings subclass for weekly api call'''
    forwardeps: Optional[float] = None
    trailingeps: Optional[float] = None
    
class Weekly_Ownership(BaseModel):
    '''Ownership subclass for weekly api call'''
    heldpercentinsiders: Optional[float] = None
    heldpercentinstitutions: Optional[float] = None
    impliedsharesoutstanding: Optional[str] = None
    floatshares: Optional[int] = None
    sharesoutstanding: Optional[int] = None
    
class Weekly_Balance(BaseModel):
    ''' Balance subclass for weekly api call'''
    totalassets: Optional[str] = None
    totalcash: Optional[int] = None
    totalcashpershare: Optional[float] = None
    totaldebt: Optional[int] = None
    totalrevenue: Optional[int] = None
    grossprofits: Optional[int] = None
    operatingcashflow: Optional[int] = None
    
    

#to have common attributes when reading or creating
class WeeklyBase(BaseModel):
    
    id: Weekly_Id | None = None
    
    general: Union[Weekly_General, None] = None
    
    analysts: Union[Weekly_Analysts, None] = None
    
    value: Union[Weekly_Value, None] = None
    
    dividends: Union[Weekly_Dividend, None] = None
    
    growth: Union[Weekly_Growth, None] = None
    
    price: Union[Weekly_Price, None] = None
    
    momentum: Union[Weekly_Momentum, None] = None
    
    earnings: Union[Weekly_Earnings, None] = None
    
    ownership : Union[Weekly_Ownership, None] = None
    
    balance : Union[Weekly_Balance, None] = None  

    
class WeeklyCreate(WeeklyBase):
    pass

'''QUARTERLY Pydantic models / schemas '''

class MoatqBase(BaseModel):
    operatingmargin: Optional[float] = None
    fcfmargin: Optional[float] = None
    roa: Optional[float] = None
    roe: Optional[float] = None
    moatpercentage: Optional[float] = None
    year: str
    ticker: str
    key: str
    
class HealthqBase(BaseModel):
    receivablessales: Optional[float] = None
    currentratio: Optional[float] = None
    financialleverage: Optional[float] = None
    debtequity: Optional[float] = None
    percentage: Optional[float] = None
    year: str
    ticker: str
    key: str
    
class FinancialsqBase(BaseModel):
    assetturnover: Optional[float] = None
    cashdebt: Optional[float] = None
    currentratio: Optional[float] = None
    debtequity: Optional[float] = None
    equityasset: Optional[float] = None
    equitymultipl: Optional[float] = None
    fcfmargin: Optional[float] = None
    financialleverage: Optional[float] = None
    goodwillassets: Optional[float] = None
    netmargin: Optional[float] = None
    operatingmargin: Optional[float] = None
    receivablessales: Optional[float] = None
    roa: Optional[float] = None
    roe: Optional[float] = None
    roic: Optional[float] = None
    year: str
    ticker:str
    key: str
    
class GrowthqBase(BaseModel):
    capitalexpenditures: Optional[float] = None
    cash: Optional[float] = None
    fcf: Optional[float] = None
    goodwill: Optional[float] = None
    netincome: Optional[float] = None
    revenue: Optional[float] = None
    longtermdebt: Optional[float] = None
    assetturnover: Optional[float] = None
    fcfmargin: Optional[float] = None
    netmargin: Optional[float] = None
    operatingmargin: Optional[float] = None
    roa: Optional[float] = None
    roe: Optional[float] = None
    roic: Optional[float] = None
    currentratio: Optional[float] = None
    financialleverage: Optional[float] = None
    receivablessales: Optional[float] = None
    debtequity: Optional[float] = None
    equityasset: Optional[float] = None
    goodwillassets: Optional[float] = None
    year: str
    ticker:str
    key: str

'''YEARLY Pydantic models / schemas '''

class MoatyBase(BaseModel):
    operatingmargin: Optional[float] = None
    fcfmargin: Optional[float] = None
    roa: Optional[float] = None
    roe: Optional[float] = None
    moatpercentage: Optional[float] = None
    year: str
    ticker: str
    key: str
    
class HealthyBase(BaseModel):
    receivablessales: Optional[float] = None
    currentratio: Optional[float] = None
    financialleverage: Optional[float] = None
    debtequity: Optional[float] = None
    percentage: Optional[float] = None
    year: str
    ticker: str
    key: str
    
class FinancialsyBase(BaseModel):
    assetturnover: Optional[float] = None
    cashdebt: Optional[float] = None
    currentratio: Optional[float] = None
    debtequity: Optional[float] = None
    equityasset: Optional[float] = None
    equitymultipl: Optional[float] = None
    fcfmargin: Optional[float] = None
    financialleverage: Optional[float] = None
    goodwillassets: Optional[float] = None
    netmargin: Optional[float] = None
    operatingmargin: Optional[float] = None
    receivablessales: Optional[float] = None
    roa: Optional[float] = None
    roe: Optional[float] = None
    roic: Optional[float] = None
    year: str
    ticker:str
    key: str
    
class GrowthyBase(BaseModel):
    capitalexpenditures: Optional[float] = None
    cash: Optional[float] = None
    fcf: Optional[float] = None
    goodwill: Optional[float] = None
    netincome: Optional[float] = None
    revenue: Optional[float] = None
    longtermdebt: Optional[float] = None
    assetturnover: Optional[float] = None
    fcfmargin: Optional[float] = None
    netmargin: Optional[float] = None
    operatingmargin: Optional[float] = None
    roa: Optional[float] = None
    roe: Optional[float] = None
    roic: Optional[float] = None
    currentratio: Optional[float] = None
    financialleverage: Optional[float] = None
    receivablessales: Optional[float] = None
    debtequity: Optional[float] = None
    equityasset: Optional[float] = None
    goodwillassets: Optional[float] = None
    year: str
    ticker:str
    key: str
    
class Prices(PricesBase):
    index: int
    #owner_id: int

    class Config:
        #orm_mode will tell the Pydantic model to read the data even if it is not a dict, but an ORM model
        orm_mode = True
    
'''QUARTERLY Pydantic models / schemas for reading / returning'''
class Weekly(WeeklyBase):
    index: int
    #owner_id: int

    class Config:
        #orm_mode will tell the Pydantic model to read the data even if it is not a dict, but an ORM model
        orm_mode = True
        
class Tick(BaseModel):
    # Schema to only get back ticker
    ticker: str
    #owner_id: int
    class Config:
        #orm_mode will tell the Pydantic model to read the data even if it is not a dict, but an ORM model
        orm_mode = True
        
        
class Moatq(MoatqBase):
    index: int
    
    class Config:
        orm_mode = True
        
class Healthq(HealthqBase):
    index: int
    
    class Config:
        orm_mode = True

class Financialsq(FinancialsqBase):
    index: int
    
    class Config:
        orm_mode = True

class Growthq(FinancialsqBase):
    index: int
    
    class Config:
        orm_mode = True
        
'''QUARTERLY Pydantic models / schemas for reading / returning'''
    
class Moaty(MoatqBase):
    index: int
    
    class Config:
        orm_mode = True
        
class Healthy(HealthqBase):
    index: int
    
    class Config:
        orm_mode = True

class Financialsy(FinancialsqBase):
    index: int
    
    class Config:
        orm_mode = True

class Growthy(FinancialsqBase):
    index: int
    
    class Config:
        orm_mode = True