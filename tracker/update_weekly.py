import numpy as np
from tracker.data_yahoo import Yahoo
import time
import pandas as pd
from sqlalchemy import create_engine, text
from random import sample
import os
from dotenv import dotenv_values
from tracker.utils import copy_from_stringio
from tracker.api_connection import get_all_tickers
import requests, urllib3


try:
    SQLALCHEMY_DATABASE_URL = f"postgresql://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}@{os.environ['POSTGRES_SERVER']}:{os.environ['POSTGRES_PORT']}/{os.environ['POSTGRES_DB']}"
    print(SQLALCHEMY_DATABASE_URL)
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
except KeyError:
    database_env = dotenv_values("database.env")
    SQLALCHEMY_DATABASE_URL = f"postgresql://{database_env['POSTGRES_USER']}:{database_env['POSTGRES_PASSWORD']}@localhost:{database_env['POSTGRES_PORT']}/{database_env['POSTGRES_DB']}"
    engine = create_engine(SQLALCHEMY_DATABASE_URL)

'''function to update weekly data'''

def update_weekly(ticker, engine):
    full = Yahoo(ticker)
    #try weekly info
    try:
        info = full.get_info()
        copy_from_stringio(info, 'weekly_info', engine)
        print(f"i - {ticker} - {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))}")
    except AttributeError:
            print(f'Attribute error for i {ticker} - {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))}')
            pass
    except KeyError:
            print(f'Key error for i {ticker} - {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))}')
            pass
    except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError, urllib3.exceptions.ProtocolError):
            time.sleep(30)
            print(f'Connection error for i {ticker} - {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))}')
            pass
    except ValueError:
            print(f'Value error for i {ticker} - probably delisted - {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))}')
            pass
    
    #try prices
    try:
        info = full.get_info()
        copy_from_stringio(info, 'weekly_info', engine)
        print(f"i - {ticker} - {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))}")
    except AttributeError:
            print(f'Attribute error for i {ticker} - {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))}')
            pass
    except KeyError:
            print(f'Key error for i {ticker} - {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))}')
            pass
    except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError, urllib3.exceptions.ProtocolError):
            time.sleep(30)
            print(f'Connection error for i {ticker} - {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))}')
            pass
    except ValueError:
            print(f'Value error for i {ticker} - probably delisted - {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))}')
            pass
        
            
if __name__ == '__main__':
        tickers = get_all_tickers()
        for ticker in tickers:
                update_weekly(ticker, engine)