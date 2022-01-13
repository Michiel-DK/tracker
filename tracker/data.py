from iexfinance.stocks import Stock
import requests
import urllib.parse
import requests
import pandas as pd
import datetime
import time
import os
from dotenv import load_dotenv
from pathlib import Path
dotenv_path = Path('../.env')
load_dotenv(dotenv_path=dotenv_path)


BASE_URL = 'https://sandbox.iexapis.com'
SANDBOX_TOKEN = os.getenv('SANDBOX_TOKEN')


class Data:
    """Class to retrieve data from multiple sources"""
    def __init__(self, ticker, timing, length):
        self.ticker = ticker
        self.timing = timing
        self.length = length
    
    def get_financials(self):
        """get financials from iex api"""
        financials_url = f"{BASE_URL}/stable/stock/{self.ticker}/financials?period={self.timing}&last={self.length}&token={SANDBOX_TOKEN}"
        financials_json = requests.get(financials_url).json()
        return pd.DataFrame(financials_json['financials'])
    
    def preprocess(self):
        """preprocess date and column names"""
        financials = self.get_financials()
        
        financials.rename(str.lower, axis='columns', inplace=True)
        financials['fiscaldate'] = pd.to_datetime(financials['fiscaldate']).dt.strftime('%Y%m')
        #v.set_index(v['fiscaldate'], inplace=True)
        financials['ticker'] = self.ticker
        return financials
    
    def add_fundamentals(self):
        financials = self.preprocess()
        
        """add profitability data"""
        financials['fcf'] = financials['cashflow'] + financials['researchanddevelopment']
        financials['operating_margin'] = financials['operatingincome'] / financials['revenue']
        financials['net_margin'] = financials['netincome'] / financials['revenue']
        financials['asset_turnover'] = financials['revenue'] / financials['totalassets']
        financials['roa'] = financials['netincome']*4/ financials['totalassets']
        financials['equity_multipl'] = financials['totalassets'] / financials['shareholderequity']
        financials['roe'] = financials['netincome'] / financials['shareholderequity']
        financials['fcf_margin'] = financials['fcf'] / financials['revenue']
        
        """add financial security data"""
        financials['cash_debt'] = financials['totalcash'] / financials['totaldebt']
        financials['equity_asset'] = financials['shareholderequity'] / financials['totalassets']
        financials['debt_equity'] = financials['totaldebt'] / financials['shareholderequity']
        financials['debt_ebitda'] = financials['totaldebt'] / (financials['ebitda']*4)
        
        return financials
        
        