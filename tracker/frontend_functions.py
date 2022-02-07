import psycopg2
from tracker.postgres import connect, config
import pandas as pd

params = config(filename='/Users/admin/code/Michiel-DK/tracker/database.ini', section='postgresql')

conn = psycopg2.connect(**params)

def get_quarterly_moat(ticker):
    cur = conn.cursor()
    cur.execute(f"""SELECT * from quarterly_moat WHERE ticker = '{ticker}'""")
    selected_moat = cur.fetchall()
    cur.close();
    colnames = [desc[0] for desc in cur.description]
    selected_moat_df = pd.DataFrame(selected_moat, columns=colnames).drop(columns='index')
    selected_moat_df.index = selected_moat_df['year']
    selected_moat_df.drop(columns = ['year', 'ticker', 'key'], inplace=True)
    return selected_moat_df

def get_quarterly_health(ticker):
    cur = conn.cursor()
    cur.execute(f"""SELECT * from quarterly_health WHERE ticker = '{ticker}'""")
    selected_moat = cur.fetchall()
    cur.close();
    colnames = [desc[0] for desc in cur.description]
    selected_health_df = pd.DataFrame(selected_moat, columns=colnames).drop(columns='index')
    selected_health_df.index = selected_health_df['year']
    selected_health_df.drop(columns = ['year', 'ticker', 'key'], inplace=True)
    return selected_health_df


def get_yearly_moat(ticker):
    cur = conn.cursor()
    cur.execute(f"""SELECT * from yearly_moat WHERE ticker = '{ticker}'""")
    selected_moat = cur.fetchall()
    cur.close();
    colnames = [desc[0] for desc in cur.description]
    selected_moat_df = pd.DataFrame(selected_moat, columns=colnames).drop(columns='index')
    selected_moat_df.index = selected_moat_df['year']
    selected_moat_df.drop(columns = ['year', 'ticker', 'key'], inplace=True)
    return selected_moat_df

def get_yearly_health(ticker):
    cur = conn.cursor()
    cur.execute(f"""SELECT * from yearly_health WHERE ticker = '{ticker}'""")
    selected_moat = cur.fetchall()
    cur.close();
    colnames = [desc[0] for desc in cur.description]
    selected_health_df = pd.DataFrame(selected_moat, columns=colnames).drop(columns='index')
    selected_health_df.index = selected_health_df['year']
    selected_health_df.drop(columns = ['year', 'ticker', 'key'], inplace=True)
    return selected_health_df

def get_weekly(ticker):
    cur = conn.cursor()
    cur.execute(f"""SELECT * from weekly_info WHERE ticker = '{ticker}'""")
    weekly = cur.fetchall()
    cur.close();
    colnames = [desc[0] for desc in cur.description]
    weekly_info = pd.DataFrame(weekly, columns=colnames).drop(columns='index')
    weekly_info.index = weekly_info['date']
    company_info = weekly_info[['ticker','logo_url','sector', 'marketcap', 'market', 'longname', 'longbusinesssummary', 'industry', 'enterprisevalue']]
    company_value = weekly_info[['trailingpe', 'trailingeps', 'totalcashpershare', 'revenuepershare', 'pricetosalestrailing12months', 'pegratio','forwardpe', 'forwardeps', 'enterprisetorevenue', 'enterprisetoebitda', 'beta'  ]]
    company_div = weekly_info[['dividendrate', 'dividendyield', 'exdividenddate', 'fiveyearavgdividendyield', 'lastdividenddate', 'lastdividendvalue']]
    company_momentum = weekly_info[['fiftytwoweeklow', 'fiftydayaverage', 'fiftytwoweekhigh', 'currentprice']]
    company_recom = weekly_info[['targetmedianprice', 'targetmeanprice', 'targetlowprice', 'targethighprice', 'regularmarketprice', 'recommendationkey', 'recommendationmean']]
    return company_info, company_value, company_div, company_momentum, company_recom