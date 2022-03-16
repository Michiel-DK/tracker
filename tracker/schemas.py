from typing import List, Optional

from pydantic import BaseModel


'''initial Pydantic models / schemas '''
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
    
'''Pydantic models / schemas for reading / returning'''
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