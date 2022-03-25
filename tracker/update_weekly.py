from tracker.data_yahoo import Yahoo
from tracker.api_connection import get_all_tickers
from sqlalchemy import create_engine
import os, requests, urllib3, time
from tracker.utils import copy_from_stringio
from dotenv import load_dotenv


load_dotenv()

SQLALCHEMY_DATABASE_URL=os.environ.get('DATABASE_URL')

engine = create_engine(SQLALCHEMY_DATABASE_URL)

'''function to update weekly data'''

def update_weekly(ticker, engine):
    full = Yahoo(ticker, full="n")
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