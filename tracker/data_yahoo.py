import pandas as pd
import yfinance as yf
from tracker.utils import reduce_memory_usage

class Yahoo:
    """Class to retrieve data Yahoo finance app"""
    def __init__(self, ticker):
        self.ticker = ticker

    def get_financials(self):
        """get financials from yahoo"""
        tick = yf.Ticker(self.ticker)
        
        #get cashflow statement
        cashflow = tick.cashflow.copy()
        cashflow.columns = [x.year for x in list(cashflow.columns)]
        
        #get balance sheet
        balance = tick.balance_sheet.copy()
        balance.columns = [x.year for x in list(balance.columns)]
        
        #get income sheet
        income = tick.earnings.copy().sort_values(by='Year', ascending=False).T

        #combine in one df
        frames = [cashflow, balance, income]
        combo = pd.concat(frames).T
        combo.columns = [x.replace(' ','').lower() for x in list(combo.columns)]
        
        return reduce_memory_usage(combo)
    
    def preprocess(self):
        """preprocess data"""
        financials = self.get_financials()
        ticker = self.ticker
        financials = financials.reset_index().rename(columns={'index':'year'})
        financials.fillna(0, inplace=True)
        financials = financials.astype('int')
        financials['ticker'] = ticker
        financials.sort_index(inplace=True)
        financials['cashflow'] = financials['totalcashfromoperatingactivities']

        
        return reduce_memory_usage(financials)
    
    def add_fundamentals(self):
        """add fundamental ratio"""
        financials = self.preprocess()

        """add profitability data"""
        try:
            financials['fcf'] = financials['totalcashfromoperatingactivities'] - abs(financials['capitalexpenditures'])
        except KeyError:
            financials['fcf'] = financials['totalcashfromoperatingactivities']
        #operatin margin deviates
        financials['operatingmargin'] = financials['totalcashfromoperatingactivities'] / financials['revenue']
        financials['netmargin'] = financials['netincome']/financials['revenue']
        financials['assetturnover'] = financials['revenue']/financials['totalassets']
        financials['roa'] = financials['netmargin'] / financials['assetturnover'] 
        financials['roe'] = financials['netmargin'] * financials['assetturnover'] * (financials['totalassets'] / financials['totalstockholderequity'])
        financials['equitymultipl'] = financials['totalassets'] / (financials['long_term_debt'] + financials['short_long_term_debt'])
        financials['fcfmargin'] = financials['fcf'] / financials['revenue']

        """add financial security data"""
        financials['cashdebt'] = financials['cash'] / (financials['long_term_debt'] + financials['short_long_term_debt'])
        financials['equityasset'] = financials['total_stockholder_equity'] / financials['totalassets']
        financials['debtequity'] = financials['longtermdebt'] / financials['totalstockholderequity']
        financials['financialleverage'] =  financials['totalassets'] / financials['totalstockholderequity']
        financials['currentratio'] = financials['totalcurrent_assets'] / financials['totalcurrentliabilities']
        try:
            financials['goodwillassets'] = financials['goodwill'] / financials['totalcurrentassets']
        except KeyError:
            pass
        financials['receivablessales'] = financials['netreceivables'] / financials['revenue']
        
        return reduce_memory_usage(financials)

if __name__ == '__main__':
    tri = Yahoo('TRI.PA').add_fundamentals()
    print(tri)