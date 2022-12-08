from tracker.data_yahoo import Yahoo
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import os, requests, urllib3, time
from tracker.utils import copy_from_stringio
from dotenv import load_dotenv
import pandas as pd
import numpy as np

load_dotenv()

SQLALCHEMY_DATABASE_URL=os.environ.get('DATABASE_URL')

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Session = sessionmaker(bind=engine)


def get_random_tick():
        
        ''' database call for random ticker symbol'''
        
        session = Session()
        query = text("SELECT ticker FROM weekly_info ORDER BY random() LIMIT 1")
        all_ticks = session.execute(query).one()
        session.close()
        return all_ticks[0]

def update_weekly(ticker, engine):
        
        ''' update weekly table'''
        
        full = Yahoo(ticker, full="y")
        info = full.get_info()
        copy_from_stringio(info, 'weekly_info', engine)
        print(f"i - {ticker} - {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))}")
        prices = full.get_prices()
        copy_from_stringio(prices, 'prices', engine)
        print(f"p - {ticker} - {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))}")

if __name__ == '__main__':
        start = time.localtime(time.time())
        ticker = get_random_tick()
        print(f"Started run at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))} for {ticker}")
        try:
                update_weekly(ticker, engine)
        except AttributeError as a:
                print(f'Attribute error for i {ticker}')
                print(a)
                pass
        except KeyError as e:
                print(f'Key error for i {ticker}')
                print(e)
                pass
        except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError, urllib3.exceptions.ProtocolError):
                time.sleep(30)
                print(f'Connection error for i {ticker}')
                pass
        except ValueError as v:
                print(f'Value error for i {ticker} - probably delisted')
                print(v)
                pass
