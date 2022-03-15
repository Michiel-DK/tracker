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

'''Pydantic models / schemas for reading / returning'''
class Weekly(WeeklyBase):
    index: int
    #owner_id: int

    class Config:
        #orm_mode will tell the Pydantic model to read the data even if it is not a dict, but an ORM model
        orm_mode = True