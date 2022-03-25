from tracker.data_yahoo import Yahoo
from tracker.api_connection import get_all_tickers
from sqlalchemy import create_engine
import os, requests, urllib3, time
from tracker.utils import copy_from_stringio
from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URL=os.environ.get('DATABASE_URL')

engine = create_engine(SQLALCHEMY_DATABASE_URL)

def update_quarter(ticker, engine):
    full = Yahoo(ticker)
    fundamentals = full.get_fundamentals()
    copy_from_stringio(fundamentals, 'yearly_financials', engine)
    moat, health = full.get_checklist()
    copy_from_stringio(moat, 'yearly_moat', engine)
    copy_from_stringio(health, 'yearly_health', engine)
    growth = full.get_growth()
    copy_from_stringio(growth, 'yearly_growth', engine)
    print(f"y - {ticker} - {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))}")
    
if __name__ == '__main__':
    tickers = get_all_tickers()
    for ticker in tickers:
        try:
            update_quarter(ticker, engine)
        except AttributeError:
                print(f'Attribute error for y {ticker}')
                continue
        except KeyError:
                print(f'Key error for y {ticker}')
                continue
        except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError, urllib3.exceptions.ProtocolError):
                time.sleep(30)
                print(f'Connection error for y {ticker}')
                continue
        except ValueError:
                print(f'Value error for y {ticker} - probably delisted')
                continue
            