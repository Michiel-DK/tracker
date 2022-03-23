import numpy as np
from tracker.data_yahoo import Yahoo
import time
import pandas as pd
from sqlalchemy import create_engine, text
from random import sample
import os
from dotenv import dotenv_values
from tracker.utils import copy_from_stringio
import requests, urllib3

try:
    SQLALCHEMY_DATABASE_URL = f"postgresql://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}@{os.environ['POSTGRES_SERVER']}:{os.environ['POSTGRES_PORT']}/{os.environ['POSTGRES_DB']}"
    print(SQLALCHEMY_DATABASE_URL)
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
except KeyError:
    database_env = dotenv_values("database.env")
    SQLALCHEMY_DATABASE_URL = f"postgresql://{database_env['POSTGRES_USER']}:{database_env['POSTGRES_PASSWORD']}@localhost:{database_env['POSTGRES_PORT']}/{database_env['POSTGRES_DB']}"
    engine = create_engine(SQLALCHEMY_DATABASE_URL)

def update_quarter(ticker, engine):
    full = Yahoo(ticker, timing='q')
    fundamentals = full.get_fundamentals()
    copy_from_stringio(fundamentals, 'quarterly_financials', engine)
    moat, health = full.get_checklist()
    copy_from_stringio(moat, 'quarterly_moat', engine)
    copy_from_stringio(health, 'quarterly_health', engine)
    growth = full.get_growth()
    copy_from_stringio(growth, 'quarterly_growth', engine)
    print(f"i - {ticker} - {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))}")
    
    

            