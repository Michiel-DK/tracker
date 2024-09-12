import pandas as pd
import numpy as np
import yfinance as yf
from datetime import date
from tracker.utils import reduce_memory_usage

class Yahoo:
    ### build in check if exits https://stackoverflow.com/questions/3867718/how-do-i-abort-object-instance-creation-in-python or https://stackoverflow.com/questions/43802348/python-exit-from-class-after-handling-exception
    # def __new__(cls, ticker):
    #     if len(yf.Ticker(ticker).cashflow) < 1:
    #         pass
    #     return super(Yahoo, cls).__new__(cls)
    
    """Class to retrieve data Yahoo finance app"""
    def __init__(self, ticker, timing=None, full=None):
        self.ticker = ticker
        self.timing = timing
        self.full = full
        
    def get_ticker(self):
        """get ticker class from yahoo"""
        tick = yf.Ticker(self.ticker)
        
        return tick
    
    def get_info(self):
        """get info dictionary from yahoo"""
        
        info_dict = self.get_ticker().info
        
        info_df = pd.DataFrame([info_dict], index=[date.today().strftime("%d/%m/%Y")])
        info_df.columns = [x.replace(' ','').lower() for x in list(info_df.columns)]
        info_df['companyofficers'] = info_df['companyofficers'].apply(lambda x:' '.join(x))
        
        columns = ['52WeekChange',
                    'SandP52WeekChange',
                    'address1',
                    'address2',
                    'algorithm',
                    'annualHoldingsTurnover',
                    'annualReportExpenseRatio',
                    'ask',
                    'askSize',
                    'averageDailyVolume10Day',
                    'averageVolume',
                    'averageVolume10days',
                    'beta',
                    'beta3Year',
                    'bid',
                    'bidSize',
                    'bookValue',
                    'category',
                    'circulatingSupply',
                    'city',
                    'companyOfficers',
                    'country',
                    'currency',
                    'currentPrice',
                    'currentRatio',
                    'dateShortInterest',
                    'dayHigh',
                    'dayLow',
                    'debtToEquity',
                    'dividendRate',
                    'dividendYield',
                    'earningsGrowth',
                    'earningsQuarterlyGrowth',
                    'ebitda',
                    'ebitdaMargins',
                    'enterpriseToEbitda',
                    'enterpriseToRevenue',
                    'enterpriseValue',
                    'exDividendDate',
                    'exchange',
                    'exchangeTimezoneName',
                    'exchangeTimezoneShortName',
                    'expireDate',
                    'fax',
                    'fiftyDayAverage',
                    'fiftyTwoWeekHigh',
                    'fiftyTwoWeekLow',
                    'financialCurrency',
                    'fiveYearAverageReturn',
                    'fiveYearAvgDividendYield',
                    'floatShares',
                    'forwardEps',
                    'forwardPE',
                    'freeCashflow',
                    'fromCurrency',
                    'fullTimeEmployees',
                    'fundFamily',
                    'fundInceptionDate',
                    'gmtOffSetMilliseconds',
                    'grossMargins',
                    'grossProfits',
                    'heldPercentInsiders',
                    'heldPercentInstitutions',
                    'impliedSharesOutstanding',
                    'industry',
                    'isEsgPopulated',
                    'lastCapGain',
                    'lastDividendDate',
                    'lastDividendValue',
                    'lastFiscalYearEnd',
                    'lastMarket',
                    'lastSplitDate',
                    'lastSplitFactor',
                    'legalType',
                    'logo_url',
                    'longBusinessSummary',
                    'longName',
                    'market',
                    'marketCap',
                    'maxAge',
                    'maxSupply',
                    'messageBoardId',
                    'morningStarOverallRating',
                    'morningStarRiskRating',
                    'mostRecentQuarter',
                    'navPrice',
                    'netIncomeToCommon',
                    'nextFiscalYearEnd',
                    'numberOfAnalystOpinions',
                    'open',
                    'openInterest',
                    'operatingCashflow',
                    'operatingMargins',
                    'payoutRatio',
                    'pegRatio',
                    'phone',
                    'preMarketPrice',
                    'previousClose',
                    'priceHint',
                    'priceToBook',
                    'priceToSalesTrailing12Months',
                    'profitMargins',
                    'quickRatio',
                    'quoteType',
                    'recommendationKey',
                    'recommendationMean',
                    'regularMarketDayHigh',
                    'regularMarketDayLow',
                    'regularMarketOpen',
                    'regularMarketPreviousClose',
                    'regularMarketPrice',
                    'regularMarketVolume',
                    'returnOnAssets',
                    'returnOnEquity',
                    'revenueGrowth',
                    'revenuePerShare',
                    'revenueQuarterlyGrowth',
                    'sector',
                    'sharesOutstanding',
                    'sharesPercentSharesOut',
                    'sharesShort',
                    'sharesShortPreviousMonthDate',
                    'sharesShortPriorMonth',
                    'shortName',
                    'shortPercentOfFloat',
                    'shortRatio',
                    'startDate',
                    'state',
                    'strikePrice',
                    'symbol',
                    'targetHighPrice',
                    'targetLowPrice',
                    'targetMeanPrice',
                    'targetMedianPrice',
                    'threeYearAverageReturn',
                    'toCurrency',
                    'totalAssets',
                    'totalCash',
                    'totalCashPerShare',
                    'totalDebt',
                    'totalRevenue',
                    'tradeable',
                    'trailingAnnualDividendRate',
                    'trailingAnnualDividendYield',
                    'trailingEps',
                    'trailingPE',
                    'trailingPegRatio',
                    'twoHundredDayAverage',
                    'volume',
                    'volume24Hr',
                    'volumeAllCurrencies',
                    'website',
                    'yield',
                    'ytdReturn',
                    'zip']
        
        empty = pd.DataFrame(columns=columns, index=[date.today().strftime("%m/%d/%Y")])
        empty.columns = [x.replace(' ','').lower() for x in list(empty.columns)]
                
        info_combo = empty.merge(info_df, how='right').set_index(empty.index)
        
        info_combo = info_combo[[x.replace(' ','').lower() for x in list(empty.columns)]]
        
        info_combo.rename(columns={'52weekchange': 'weekchange52'}, inplace=True)
        
        info_combo['longbusinesssummary'] = info_combo['longbusinesssummary'].apply(lambda x: x.replace(';', ' '))
        
        int = ['targetlowprice',
                'targetmedianprice',
                'currentprice',
                'targetmeanprice',
                'targethighprice',
                'previousclose',
                'regularmarketopen',
                'twohundreddayaverage',
                'regularmarketdayhigh',
                'regularmarketpreviousclose',
                'fiftydayaverage',
                'open',
                'regularmarketdaylow',
                'daylow',
                'ask',
                'fiftytwoweekhigh',
                'fiftytwoweeklow',
                'bid',
                'dayhigh',
                'regularmarketprice',
                'premarketprice']
        
        to_change = info_combo[int].select_dtypes('int64').columns
        
        info_combo[to_change] = info_combo[to_change].astype('float')
        
        info_combo = info_combo.reset_index().rename(columns={'symbol':'ticker', 'index':'date'})
        
        info_combo['key'] = info_combo['date'].astype('str') + info_combo['ticker']
        
        #info_combo.fillna('null', inplace=True)
        
        return info_combo
    
    def get_prices(self):
        tick = self.get_ticker()
        if self.full == 'y':
            prices = tick.history(period="max")
        prices = tick.history(period="1wk")
        
        prices.reset_index(inplace=True)
        prices.columns = [x.replace(' ','').lower() for x in list(prices.columns)]
        prices['ticker'] = self.ticker
        prices['key'] = prices['date'].apply(lambda x: x.strftime("%Y/%m/%d") + "-" + self.ticker)
        
        columns = ['date',
                   'open',
                   'high',
                   'low',
                   'close',
                   'volume',
                   'dividends',
                   'stocksplits',
                   'ticker',
                   'key']
        
        empty = pd.DataFrame(columns=columns, index=prices.index)
        
        empty['date'] = empty['date'].astype('datetime64[ns]')
                    
        combo_merged = empty.merge(prices, how='right').set_index(empty.index)
        
        combo_merged.dropna(inplace=True)
        
        #combo_merged = combo_merged.fillna(0).astype('float').astype('int')
        
        combo_merged[['volume', 'dividends', 'stocksplits']] = combo_merged[['volume', 'dividends', 'stocksplits']].astype('int')
            
        return combo_merged
        

    def get_financials(self):
        """get financials from yahoo"""
        tick = self.get_ticker()
        timing = self.timing
        
        if timing == "q":
            cashflow = tick.quarterly_cashflow.copy()
            cashflow.columns = [f"{i.year}Q{i.quarter}" for i in list(cashflow.columns)]
            balance = tick.quarterly_balance_sheet.copy()
            balance.columns = [f"{i.year}Q{i.quarter}" for i in list(balance.columns)]
            income = tick.quarterly_earnings.copy().sort_values(by='Quarter', ascending=False).T
            income.columns = [f"{i[-4:]}{i[1]}{i[0]}" for i in list(income.columns)]
        else:
            cashflow = tick.cashflow.copy()
            cashflow.columns = [x.year for x in list(cashflow.columns)]
            balance = tick.balance_sheet.copy()
            balance.columns = [x.year for x in list(balance.columns)]
            income = tick.earnings.copy().sort_values(by='Year', ascending=False).T
            
        if income.columns.nunique() < 4:
            raise KeyError
        
        else:
            
            #combine in one df
            frames = [cashflow, balance, income]
            combo = pd.concat(frames).T
            combo.columns = [x.replace(' ','').lower() for x in list(combo.columns)]
                    
            #add with total possible columns
            columns = ['accountspayable',
                        'assetturnover',
                        'capitalexpenditures',
                        'capitalsurplus',
                        'cash',
                        'cashdebt',
                        'cashflow',
                        'changeincash',
                        'changetoaccountreceivables',
                        'changetoinventory',
                        'changetoliabilities',
                        'changetonetincome',
                        'changetooperatingactivities',
                        'commonstock',
                        'currentratio',
                        'debtequity',
                        'deferredlongtermassetcharges',
                        'deferredlongtermliab',
                        'depreciation',
                        'dividendspaid',
                        'earnings',
                        'effectofexchangerate',
                        'equityasset',
                        'equitymultipl',
                        'fcf',
                        'fcfmargin',
                        'financialleverage',
                        'goodwill',
                        'goodwillassets',
                        'intangibleassets',
                        'inventory',
                        'investments',
                        'issuanceofstock',
                        'longtermdebt',
                        'longterminvestments',
                        'minorityinterest',
                        'netborrowings',
                        'netincome',
                        'netmargin',
                        'netreceivables',
                        'nettangibleassets',
                        'operatingmargin',
                        'otherassets',
                        'othercashflowsfromfinancingactivities',
                        'othercashflowsfrominvestingactivities',
                        'othercurrentassets',
                        'othercurrentliab',
                        'otherliab',
                        'otherstockholderequity',
                        'propertyplantequipment',
                        'receivablessales',
                        'repurchaseofstock',
                        'retainedearnings',
                        'revenue',
                        'roa',
                        'roe',
                        'roic',
                        'shortlongtermdebt',
                        'shortterminvestments',
                        'ticker',
                        'totalassets',
                        'totalcashflowsfrominvestingactivities',
                        'totalcashfromfinancingactivities',
                        'totalcashfromoperatingactivities',
                        'totalcurrentassets',
                        'totalcurrentliabilities',
                        'totalliab',
                        'totalstockholderequity',
                        'treasurystock']
            
            empty = pd.DataFrame(columns=columns, index=combo.index)
                    
            combo_merged = empty.merge(combo, how='right').set_index(empty.index)
            
            combo_merged = combo_merged.fillna(0).astype('int')[columns]
            
            return reduce_memory_usage(combo_merged)
    
    def get_preprocess(self):
        """preprocess data"""
        financials = self.get_financials()
        ticker = self.ticker
        timing = self.timing
        
        financials = financials.reset_index().rename(columns={'index':'year'})
        #financials.fillna(0, inplace=True)
        #financials = financials.astype('int')
        financials['ticker'] = ticker
        financials.sort_index(inplace=True)
        financials['cashflow'] = financials['totalcashfromoperatingactivities']
        
        financials['key'] = financials['year'].astype('str') + financials['ticker']
 
        
        return reduce_memory_usage(financials)
    
    def get_fundamentals(self):
        """add fundamental ratio"""
        financials = self.get_preprocess()

        """add profitability data"""
        try:
            financials['fcf'] = financials['totalcashfromoperatingactivities'] - abs(financials['capitalexpenditures'])
        except KeyError:
            financials['fcf'] = financials['totalcashfromoperatingactivities']
        #operatin margin deviates
        financials['operatingmargin'] = financials['totalcashfromoperatingactivities'] / financials['revenue']
        financials['netmargin'] = financials['netincome']/financials['revenue']
        financials['fcfmargin'] = financials['fcf'] / financials['revenue']
        financials['assetturnover'] = financials['revenue']/financials['totalassets']
        financials['roa'] = financials['netmargin'] / financials['assetturnover'] 
        financials['roe'] = financials['netmargin'] * financials['assetturnover'] * (financials['totalassets'] / financials['totalstockholderequity'])
        financials['roic'] = (financials['netincome'] - abs(financials['dividendspaid']))/(financials['shortlongtermdebt']+financials['longtermdebt']+financials['totalstockholderequity']-financials['goodwill']-financials['cash'])
        try:
            financials['equitymultipl'] = financials['totalassets'] / (financials['longtermdebt'] + financials['shortlongtermdebt'])
        except KeyError:
            try:
                financials['equitymultipl'] = financials['totalassets'] / (financials['longtermdebt'])
            except KeyError:
                try:
                    financials['equitymultipl'] = financials['totalassets'] / (financials['shortlongtermdebt'])
                except KeyError:
                    financials['equitymultipl'] = np.nan
            
            

        """add financial security data"""
        try:
            financials['cashdebt'] = financials['cash'] / (financials['longtermdebt'] + financials['shortlongtermdebt'])
        except KeyError:
            try:
                financials['cashdebt'] = financials['cash'] / (financials['longtermdebt'])
            except KeyError:
                try:
                    financials['cashdebt'] = financials['cash'] / (financials['shortlongtermdebt'])
                except KeyError:
                    financials['cashdebt'] = np.nan
                
        financials['equityasset'] = financials['totalstockholderequity'] / financials['totalassets']
        try:
            financials['debtequity'] = (financials['longtermdebt'] + financials['shortlongtermdebt']) / financials['totalstockholderequity']
        except KeyError:
            financials['debtequity'] = np.nan
            
        financials['financialleverage'] =  financials['totalassets'] / financials['totalstockholderequity']
        financials['currentratio'] = financials['totalcurrentassets'] / financials['totalcurrentliabilities']
        try:
            financials['goodwillassets'] = financials['goodwill'] / financials['totalcurrentassets']
        except KeyError:
            financials['goodwillassets'] = np.nan
        financials['receivablessales'] = financials['netreceivables'] / financials['revenue']
        
        return reduce_memory_usage(financials)
    
    def get_checklist(self):
        financials = self.get_fundamentals()
        
        """add moat checklist"""
        moat = pd.DataFrame()
        moat['operatingmargin'] = financials['operatingmargin'].apply(lambda x: x/0.15)
        moat['fcfmargin'] = financials['fcfmargin'].apply(lambda x: x/0.05)
        moat['netmargin'] = financials['netmargin'].apply(lambda x: x/0.15)
        moat['roa'] = financials['netmargin'].apply(lambda x: x/0.06)
        moat['roe'] = financials['netmargin'].apply(lambda x: x/0.01)
        moat['average'] = moat.sum(axis=1)/moat.count(axis=1)
        moat['year'] = financials['year']
        moat['ticker'] = financials['ticker']
        moat['key'] = financials['key']

        """add financial health checklist"""
        health = pd.DataFrame()
        try:
            health['receivablessales'] = financials['receivablessales'].apply(lambda x: 0.25/x) #low
        except ZeroDivisionError:
            health['receivablessales'] = np.nan
        health['currentratio'] = financials['currentratio'].apply(lambda x: x/1)
        try:
            health['financialleverage'] = financials['financialleverage'].apply(lambda x: 4/x) #low
        except ZeroDivisionError:
            health['financialleverage'] = np.nan
        try:
            health['debtequity'] = financials['debtequity'].apply(lambda x: 1.5/x) #low
        except ZeroDivisionError:
            health['debtequity'] = np.nan
        health['average'] = health.sum(axis=1)/health.count(axis=1)
        health['year'] = financials['year']
        health['ticker'] = financials['ticker']
        health['key'] = financials['key']
        
        return reduce_memory_usage(moat), reduce_memory_usage(health)

    def get_growth(self):
        pd.options.mode.chained_assignment = None
        fundamentals = self.get_fundamentals().sort_values(by='year', ascending=True)
        
        growth = fundamentals\
            [['capitalexpenditures', 'cash', 'fcf', 'goodwill', 'netincome', 'revenue', 'longtermdebt', \
            'assetturnover', 'fcfmargin', 'netmargin', 'operatingmargin', 'roa', 'roe', 'roic',\
                'currentratio', 'financialleverage', 'receivablessales', 'debtequity', 'equityasset', 'goodwillassets']]
            
        floats = ['assetturnover', 'fcfmargin', 'netmargin', 'operatingmargin', 'roa', 'roe', 'roic',\
                'currentratio', 'financialleverage', 'receivablessales', 'debtequity', 'equityasset', 'goodwillassets']
        
        growth[floats] = growth.loc[:,floats].astype('float32')
        
        growth = growth.pct_change()
        
        growth['ticker'] = fundamentals['ticker']
        growth['key'] = fundamentals['key']
        growth['year'] = fundamentals['year']
       
        
        return reduce_memory_usage(growth.iloc[1: , :])

        
if __name__ == '__main__':
    tri = Yahoo('SAN.PA').get_fundamentals()
    print(tri)