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
    full = Yahoo(ticker, timing='q')
    fundamentals = full.get_fundamentals()
    copy_from_stringio(fundamentals, 'quarterly_financials', engine)
    moat, health = full.get_checklist()
    copy_from_stringio(moat, 'quarterly_moat', engine)
    copy_from_stringio(health, 'quarterly_health', engine)
    growth = full.get_growth()
    copy_from_stringio(growth, 'quarterly_growth', engine)
    print(f"q - {ticker} - {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))}")
    
if __name__ == '__main__':
    tickers = get_all_tickers()
    for ticker in tickers:
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
            
