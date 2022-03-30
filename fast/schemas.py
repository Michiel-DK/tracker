from typing import List, Optional
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

'''WEEKLY Pydantic models / schemas '''
class PricesBase(BaseModel):
    date: datetime.date
    close: Optional[float] = None
    ticker: str
    key: str
    
class PricesCreate(PricesBase):
    pass

'''QUARTERLY Pydantic models / schemas '''
#to have common attributes when reading or creating
class WeeklyBase(BaseModel):
    ticker: str
    grossmargin: Optional[float] = None
    key: str
    
class WeeklyCreate(WeeklyBase):
    pass

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