from tracker.data_yahoo import Yahoo
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import os, requests, urllib3, time
from tracker.utils import copy_from_stringio
from dotenv import load_dotenv
import pandas as pd
import numpy as np

from random import sample


load_dotenv()

SQLALCHEMY_DATABASE_URL=os.environ.get('DATABASE_URL')

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Session = sessionmaker(bind=engine)

def get_random_tick():
        
        '''database call for random ticker != latest quarter'''
        
        session = Session()
        newest = text("SELECT MAX(year) FROM quarterly_financials")
        newest = session.execute(newest).one()[0]
        query = text(f"SELECT ticker FROM quarterly_financials WHERE year != '{newest}' ORDER BY random() LIMIT 1")
        tick = session.execute(query).one()[0]
        session.close()
        return tick

def update_quarter(ticker, engine):
        
        ''' update quaterly financials + adjecent tables'''
        
        full = Yahoo(ticker, timing='q')
        
        fundamentals = full.get_fundamentals()
        for i in range(len(fundamentals)):
                row = pd.DataFrame(fundamentals.iloc[i]).T
                print(row)
                copy_from_stringio(row, 'quarterly_financials', engine)
                
        moat, health = full.get_checklist()
        
        for i in range(len(moat)):
                row = pd.DataFrame(moat.iloc[i]).T
                print(row)
                copy_from_stringio(row, 'quarterly_moat', engine)
        for i in range(len(health)):
                row = pd.DataFrame(health.iloc[i]).T
                print(row)
                copy_from_stringio(row, 'quarterly_health', engine)
                
        growth = full.get_growth()
        for i in range(len(growth)):
                row = pd.DataFrame(growth.iloc[i]).T
                print(row)
                copy_from_stringio(row, 'quarterly_growth', engine)
        
        print(f"q - {ticker} - {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))}")
    
if __name__ == '__main__':
        start = time.localtime(time.time())
        ticker = get_random_tick()
        print(f"Started run at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))} for {ticker}")
        try:
                update_quarter(ticker, engine)
        except AttributeError as a:
                print(f'Attribute error for q {ticker}')
                print(a)
                pass
        except KeyError as k:
                print(f'Key error for q {ticker}')
                print(k)
                pass
        except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError, urllib3.exceptions.ProtocolError):
                time.sleep(30)
                print(f'Connection error for q {ticker}')
                pass
        except ValueError as v:
                print(f'Value error for q {ticker} - probably delisted')
                print(v)
                pass
            
