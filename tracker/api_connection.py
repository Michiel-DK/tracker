import requests


def get_all_tickers():  
    tickers = requests.get('http://api:8000/weekly_all').json()
    tickers = [x['ticker'] for x in tickers]
    return tickers
