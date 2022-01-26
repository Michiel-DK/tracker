import pandas as pd
import yfinance as yf

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
        combo.columns = [x.replace(' ','_').lower() for x in list(combo.columns)]
        
        return combo
    
    def preprocess(self):
        """preprocess data"""
        financials = self.get_financials()
        ticker = self.ticker
        financials = financials.reset_index().rename(columns={'index':'year'})
        financials['ticker'] = ticker
        
        return financials
    
    def add_fundamentals(self):
        """add fundamental ratio"""
        financials = self.preprocess()
        
        try:
            financials['fcf'] = financials['total_cash_from_operating_activities'] - abs(financials['capital_expenditures'])
        except KeyError:
            financials['fcf'] = financials['total_cash_from_operating_activities']
        financials['cashflow_operations'] = financials['total_cash_from_operating_activities']
        financials.sort_index(inplace=True)
        financials['fcf_change'] = financials.fcf.pct_change()
        financials['revenue_change'] = financials.revenue.pct_change()
        financials['cashflow_change'] = financials.cashflow_operations.pct_change()
        
        financials['net_margin'] = financials['net_income']/financials['revenue']
        financials['asset_turnover'] = financials['revenue']/financials['total_assets']
        financials['net_income/cfo'] = financials['net_income']/financials['total_cash_from_operating_activities']
        financials['cashflow_operations'] = financials['total_cash_from_operating_activities']/financials['revenue']
        financials['roa'] = financials['net_margin'] / financials['asset_turnover'] 
        financials['roe'] = financials['net_margin'] * financials['asset_turnover'] * (financials['total_assets'] / financials['total_stockholder_equity'])
        try:
            financials['fcf'] = financials['total_cash_from_operating_activities'] - abs(financials['capital_expenditures'])
        except KeyError:
            financials['fcf'] = financials['total_cash_from_operating_activities']
        financials['fcf_earnings'] = financials['fcf'] / financials['revenue']
        financials['operating_margin'] = financials['total_cash_from_operating_activities'] / financials['revenue']
        financials['financial_leverage'] =  financials['total_assets'] / financials['total_stockholder_equity']
        financials['debt_to_equity'] = financials['long_term_debt'] / financials['total_stockholder_equity']
        financials['current_ratio'] = financials['total_current_assets'] / financials['total_current_liabilities']
        try:
            financials['quick_ratio'] = (financials['total_current_assets'] + financials['inventory']) / financials['total_current_liabilities']
        except KeyError:
            financials['quick_ratio'] = financials['total_current_assets']  / financials['total_current_liabilities']
        try:
            financials['goodwill_to_assets'] = financials['good_will'] / financials['total_current_assets']
        except KeyError:
            pass
        financials['receivables_sales'] = financials['net_receivables'] / financials['revenue']
        
        return financials