from tracker.data_yahoo import Yahoo
from tracker.insert_rows import copy_from_stringio


def quarterly_import(tickers):
    for ticker in tickers:
        full = Yahoo(ticker, timing='q')
        try:
            fundamentals = full.get_fundamentals()
            copy_from_stringio(fundamentals, 'quarterly_financials')
            moat, health = full.get_checklist()
            copy_from_stringio(moat, 'quarterly_moat')
            copy_from_stringio(health, 'quarterly_health')
            growth = full.get_growth()
            copy_from_stringio(growth, 'quarterly_growth')
            print(f"q - {ticker}")
        except AttributeError:
                print(f'Attribute error for q {ticker}')
                pass
        except KeyError:
                print(f'Key error for q {ticker}')
                pass

def yearly_import(tickers):
    for ticker in tickers:
        full = Yahoo(ticker)
        try:
            fundamentals = full.get_fundamentals()
            copy_from_stringio(fundamentals, 'yearly_financials')
            moat, health = full.get_checklist()
            copy_from_stringio(moat, 'yearly_moat')
            copy_from_stringio(health, 'yearly_health')
            growth = full.get_growth()
            copy_from_stringio(growth, 'yearly_growth')
            print(f"q - {ticker}")
        except AttributeError:
                print(f'Attribute error for q {ticker}')
                pass
        except KeyError:
                print(f'Key error for q {ticker}')
                pass
            
def weekly_import(tickers):
    for ticker in tickers:
        full = Yahoo(ticker)
        try:
            info = full.get_info()
            copy_from_stringio(info, 'weekly_info')
            print(f"i - {ticker}")
        except AttributeError:
                print(f'Attribute error for i {ticker}')
                pass
        except KeyError:
                print(f'Key error for i {ticker}')
                pass