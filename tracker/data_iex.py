import requests
import pandas as pd
import os
from dotenv import load_dotenv
from pathlib import Path
from tracker.utils import reduce_memory_usage

load_dotenv()

BASE_URL = 'https://sandbox.iexapis.com'
SANDBOX_TOKEN = os.getenv('SANDBOX_TOKEN')

class Iex:
    """Class to retrieve data from multiple sources"""
    def __init__(self, ticker, timing, length):
        self.ticker = ticker
        self.timing = timing
        self.length = length
    
    def get_financials(self):
        """get financials from iex api"""
        financials_url = f"{BASE_URL}/stable/stock/{self.ticker}/financials?period={self.timing}&last={self.length}&token={SANDBOX_TOKEN}"
        financials_json = requests.get(financials_url).json()
        return reduce_memory_usage(pd.DataFrame(financials_json['financials']), verbose=True)
    
    def preprocess(self):
        """preprocess date and column names"""
        financials = self.get_financials()
        
        financials.rename(str.lower, axis='columns', inplace=True)
        financials['fiscaldate'] = pd.to_datetime(financials['fiscaldate']).dt.strftime('%Y%m')
        #v.set_index(v['fiscaldate'], inplace=True)
        financials['ticker'] = self.ticker
        financials = financials.fillna(0)
        return reduce_memory_usage(financials)
    
    def add_fundamentals(self):
        financials = self.preprocess()
        
        """add profitability data"""
        financials['fcf'] = financials['cashflow'] + financials['researchanddevelopment']
        financials['operatingmargin'] = financials['operatingincome'] / financials['revenue']
        financials['netmargin'] = financials['netincome'] / financials['revenue']
        financials['fcfmargin'] = financials['fcf'] / financials['revenue']
        financials['assetturnover'] = financials['revenue'] / financials['totalassets']
        financials['roa'] = financials['netincome']*4/ financials['totalassets']
        financials['roe'] = financials['netincome'] / financials['shareholderequity']
        
        """add financial security data"""
        financials['cashdebt'] = financials['totalcash'] / financials['totaldebt']
        financials['equityasset'] = financials['shareholderequity'] / financials['totalassets']
        financials['debtequity'] = financials['totaldebt'] / financials['shareholderequity']
        financials['financialleverage'] = financials['totalassets'] / financials['shareholderequity']
        financials['currentratio'] = financials['currentassets'] / financials['inventory']
        financials['goodwillassets'] = financials['goodwill'] / financials['currentassets']
        financials['receivablessales'] = financials['netreceivables'] / financials['revenue']
                
        return reduce_memory_usage(financials)
    
    def checklist(self):
        financials = self.add_fundamentals()
        
        """add moat checklist"""
        moat = pd.DataFrame()
        moat['net_margin'] = financials['net_margin'].apply(lambda x: 1 if x >= 0.15 else 0)
        moat['roa'] = financials['net_margin'].apply(lambda x: 1 if x >= 0.06 else 0)
        moat['roe'] = financials['net_margin'].apply(lambda x: 1 if x >= 0.1 else 0)
        moat['fcf_earnings'] = financials['fcf_earnings'].apply(lambda x: 1 if x >= 0.05 else 0)
        moat['operating_margin'] = financials['operating_margin'].apply(lambda x: 1 if x >= 0.15 else 0)
        
if __name__ == '__main__':
    adbe = Iex('LRLCF', 'quarter', '12').add_fundamentals()
    print(adbe)