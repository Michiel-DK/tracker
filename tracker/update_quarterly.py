from tracker.data_yahoo import Yahoo
from tracker.api_connection import get_all_tickers
from sqlalchemy import create_engine
import os, requests, urllib3, time
from tracker.utils import copy_from_stringio
from dotenv import load_dotenv
import pandas as pd

from random import sample


load_dotenv()

SQLALCHEMY_DATABASE_URL=os.environ.get('DATABASE_URL')

engine = create_engine(SQLALCHEMY_DATABASE_URL)

def update_quarter(ticker, engine):
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
    #tickers = get_all_tickers()
    print(f"Started run at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))}")
    full = list(pd.read_csv('../tracker/data/ticks_quart.csv', sep=';')['ticks'])
    tickers = full[:2]
    del full[:2]
    pd.DataFrame.to_csv(pd.DataFrame({'ticks': full}), '../tracker/data/ticks_quart.csv', sep=';')
    for ticker in tickers:
            print(ticker)
            try:
                    update_quarter(ticker, engine)
            except AttributeError:
                    print(f'Attribute error for q {ticker}')
                    continue
            except KeyError:
                    print(f'Key error for q {ticker}')
                    continue
            except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError, urllib3.exceptions.ProtocolError):
                    time.sleep(30)
                    print(f'Connection error for q {ticker}')
                    continue
            except ValueError:
                    print(f'Value error for q {ticker} - probably delisted')
                    continue
            
