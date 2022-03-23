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
    

def update_weekly(ticker, engine):
    full = Yahoo(ticker)
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
    start = time.time()
    not_found_q = []
    time_q = []
    not_found_y = []
    time_y = []
    not_found_i = []
    time_i = []
    not_found_p = []
    time_p = []
    #tickers = get_tickers()
    root_dir = os.path.dirname(__file__)
    csv_path = os.path.join(root_dir, "data", "euronext.csv")
    tickers = list(pd.read_csv(csv_path, sep=';')['yahoo'])
    tickers = [x.strip(' ') for x in tickers]
    tickers = sample(tickers, 2)
    for ticker in tickers:
        full = Yahoo(ticker)
        try:
            individ = time.time()
            fundamentals = full.get_fundamentals()
            copy_from_stringio(fundamentals, 'yearly_financials', engine)
            moat, health = full.get_checklist()
            copy_from_stringio(moat, 'yearly_moat')
            copy_from_stringio(health, 'yearly_health')
            growth = full.get_growth()
            copy_from_stringio(growth, 'yearly_growth')
            #print(f"time for y {ticker} : {time.time() - individ}")
            print(f"y - {ticker}")
            time_y.append(time.time() - individ)
        except AttributeError:
                print(f'Attribute error for y {ticker}')
                not_found_y.append(ticker)
                pass
        except KeyError:
                print(f'Key error for y {ticker}')
                not_found_y.append(ticker)
                pass

        try:
            individ = time.time()
            info = full.get_info()
            copy_from_stringio(info, 'weekly_info')
            #print(f"time for i {ticker} : {time.time() - individ}")
            time_i.append(time.time() - individ)
            print(f"i - {ticker}")
        except AttributeError:
                print(f'Attribute error for i {ticker}')
                not_found_i.append(ticker)
                pass
        except KeyError:
                print(f'Key error for i {ticker}')
                not_found_i.append(ticker)
                pass
            
        try:
            individ = time.time()
            prices = full.get_prices()
            print(prices)
            copy_from_stringio(prices, 'prices')
            #print(f"time for i {ticker} : {time.time() - individ}")
            time_p.append(time.time() - individ)
            print(f"p - {ticker}")
        except AttributeError:
                print(f'Attribute error for p {ticker}')
                not_found_p.append(ticker)
                pass
        except KeyError:
                print(f'Key error for p {ticker}')
                not_found_p.append(ticker)
                pass
            
    end = time.time()-start
    print(f"total run-time info: {end/60} min")
    print(f"total time i {sum(time_i)/60}, avg time i {np.mean(time_i)}")
    print(f"not found i {not_found_i}")
    print(f"total time p {sum(time_p)/60} in minutes, avg time p {np.mean(time_p)} in seconds")
    print(f"not found p {not_found_p}")
    
    
    #build in ticker check foreign + US