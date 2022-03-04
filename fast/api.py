import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from tracker.frontend_functions import *

class User(BaseModel):
    first_name: str
    last_name: str = None
    age: int
    

app = FastAPI()

@app.post("/user/", response_model=User)
async def create_user(user: User):
    return user

@app.get("/weekly_info")
async def get_weekly(ticker):
    company_info, company_value, company_div, company_momentum, company_recom = get_weekly(ticker)
    return company_info[0]["ticker"][0]

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)