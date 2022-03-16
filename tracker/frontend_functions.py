from tracker.postgres import connect, config
import pandas as pd
import numpy as np
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
import dotenv
import os

#params = config(filename='/Users/michieldekoninck/code/Michiel-DK/tracker/database.ini', section='postgresql')

#conn = psycopg2.connect(**params)

try:
    from dotenv import dotenv_values
    database_env = dotenv_values("database.env")
    engine = create_engine(f"postgresql://{database_env['POSTGRES_USER']}:{database_env['POSTGRES_PASSWORD']}@localhost:{database_env['POSTGRES_PORT']}/{database_env['POSTGRES_DB']}")
except KeyError:
    engine = create_engine(f"postgresql://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}@localhost:{os.environ['POSTGRES_PORT']}/{os.environ['POSTGRES_DB']}")

Session = sessionmaker(bind=engine)

def get_all_tickers():
    session = Session()
    query = text("SELECT DISTINCT ON (ticker) date, ticker, shortname FROM weekly_info ORDER BY ticker, date desc")
    all_ticks = session.execute(query).fetchall()
    #colnames = session.execute(query).keys()
    session.close()
    return [x[1:] for x in all_ticks]
    
    
def get_all_text():
    session = Session()
    query = text("SELECT ticker, longname, longbusinesssummary FROM weekly_info")
    data = session.execute(query).fetchall()
    colnames = session.execute(query).keys()
    df = pd.DataFrame(data, columns=colnames)
    session.close()
    return df

def get_quarterly_moat(ticker):
    #cur = conn.cursor()
    #cur.execute(f"""SELECT * from quarterly_moat WHERE ticker = '{ticker}'""")
    #selected_moat = cur.fetchall()
    #cur.close();
    #colnames = [desc[0] for desc in cur.description]
    session = Session()
    query = text(f"SELECT * from quarterly_moat WHERE ticker = '{ticker}'")
    selected_moat = session.execute(query).fetchall()
    colnames = session.execute(query).keys()
    session.close()
    selected_moat_df = pd.DataFrame(selected_moat, columns=colnames).drop(columns='index')
    selected_moat_df.index = selected_moat_df['year']
    selected_moat_df.drop(columns = ['year', 'ticker', 'key'], inplace=True)
    selected_moat_df.replace(np.inf, np.nan, inplace=True)
    return selected_moat_df

def get_quarterly_health(ticker):
    session = Session()
    query = text(f"SELECT * from quarterly_health WHERE ticker = '{ticker}'")
    selected_health = session.execute(query).fetchall()
    colnames = session.execute(query).keys()
    session.close()
    selected_health_df = pd.DataFrame(selected_health, columns=colnames).drop(columns='index')
    selected_health_df.index = selected_health_df['year']
    selected_health_df.drop(columns = ['year', 'ticker', 'key'], inplace=True)
    selected_health_df.replace(np.inf, np.nan, inplace=True)
    return selected_health_df


def get_yearly_moat(ticker):
    session = Session()
    query = text(f"SELECT * from yearly_moat WHERE ticker = '{ticker}'")
    selected_moat = session.execute(query).fetchall()
    colnames = session.execute(query).keys()
    session.close()
    selected_moat_df = pd.DataFrame(selected_moat, columns=colnames).drop(columns='index')
    selected_moat_df.index = selected_moat_df['year']
    selected_moat_df.drop(columns = ['year', 'ticker', 'key'], inplace=True)
    selected_moat_df.replace(np.inf, np.nan, inplace=True)
    return selected_moat_df

def get_yearly_health(ticker):
    session = Session()
    query = text(f"SELECT * from yearly_health WHERE ticker = '{ticker}'")
    selected_health = session.execute(query).fetchall()
    colnames = session.execute(query).keys()
    session.close()
    selected_health_df = pd.DataFrame(selected_health, columns=colnames).drop(columns='index')
    selected_health_df.index = selected_health_df['year']
    selected_health_df.drop(columns = ['year', 'ticker', 'key'], inplace=True)
    selected_health_df.replace(np.inf, np.nan, inplace=True)
    return selected_health_df

def get_weekly(ticker):
    session = Session()
    query = text(f"SELECT DISTINCT on (ticker) * from weekly_info WHERE ticker = '{ticker}' ORDER BY ticker, date desc")
    weekly = session.execute(query).fetchall()
    colnames = session.execute(query).keys()
    session.close()
    weekly_info = pd.DataFrame(weekly, columns=colnames).drop(columns='index')
    weekly_info.index = weekly_info['date']
    company_info = weekly_info[['ticker','logo_url','sector', 'marketcap', 'market', 'longname', 'longbusinesssummary', 'industry', 'enterprisevalue']]
    company_value = weekly_info[['trailingpe', 'trailingeps', 'totalcashpershare', 'revenuepershare', 'pricetosalestrailing12months', 'pegratio','forwardpe', 'forwardeps', 'enterprisetorevenue', 'enterprisetoebitda', 'beta'  ]]
    company_div = weekly_info[['dividendrate', 'dividendyield', 'exdividenddate', 'fiveyearavgdividendyield', 'lastdividenddate', 'lastdividendvalue']]
    company_momentum = weekly_info[['fiftytwoweeklow', 'fiftydayaverage', 'fiftytwoweekhigh', 'currentprice']]
    company_recom = weekly_info[['targetmedianprice', 'targetmeanprice', 'targetlowprice', 'targethighprice', 'regularmarketprice', 'recommendationkey', 'recommendationmean']]
    return company_info, company_value, company_div, company_momentum, company_recom

def get_all_companies_industry(industry):
    session = Session()
    query = text(f"SELECT ticker FROM weekly_info WHERE industry='{industry}'")
    all_comp = session.execute(query).fetchall()
    session.close()
    return [x[0] for x in all_comp]

def get_quarterly_moat_industry(industry):
    tickers = get_all_companies_industry(industry)
    session = Session()
    query = text(f"SELECT year, AVG(moatpercentage)/COUNT(moatpercentage) FROM quarterly_moat WHERE ticker in {tuple(tickers)} GROUP BY year")
    all_comp = session.execute(query).fetchall()
    colnames = session.execute(query).keys()
    all_comp_df = pd.DataFrame(all_comp, columns=colnames).set_index('year').rename(columns={'?column?':f'{industry} average'})
    return all_comp_df
    
def get_avg_weekly_industry(industry):
    session = Session()
    query = text("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'weekly_info' AND DATA_TYPE='real'")
    weekly = session.execute(query).fetchall()
    ls = [f"AVG({x[0]}) AS {x[0]}"  for x in weekly]
    query2 = text(f"SELECT industry, {', '.join(ls)} FROM weekly_info WHERE industry='{industry}' GROUP BY industry")
    weekly = session.execute(query2).fetchall()
    colnames = session.execute(query2).keys()
    session.close()
    df = pd.DataFrame(weekly, columns=colnames, index=[f'{industry} average']).T
    return df



def get_scanner_q():
    # get moat
    session = Session()
    query = text(f"SELECT * from quarterly_moat")
    moat = session.execute(query).fetchall()
    colnames = session.execute(query).keys()
    session.close()
    q_moat = pd.DataFrame(moat, columns=colnames).drop(columns='index')
    q_moat.replace(np.inf, np.nan, inplace=True)
    #get health
    session = Session()
    query = text(f"SELECT * from quarterly_health")
    health = session.execute(query).fetchall()
    colnames = session.execute(query).keys()
    session.close()
    q_health = pd.DataFrame(health, columns=colnames).drop(columns='index')
    q_health.replace(np.inf, np.nan, inplace=True)
    #get weekly
    session = Session()
    query = text("SELECT DISTINCT ON (ticker) * FROM weekly_info ORDER BY ticker, date desc")
    weekly = session.execute(query).fetchall()
    colnames = session.execute(query).keys()
    session.close()
    weekly = pd.DataFrame(weekly, columns=colnames).drop(columns='index')
    weekly = weekly[['ticker','totalcashpershare', 'enterprisetorevenue', 'enterprisetoebitda', 'beta','longname','sector', 'industry', 'market', 'country']]
    #combine
    ls = []
    for i in q_moat[q_moat['year']=='2021Q3']['ticker']:
        ls.append([i, np.round(np.mean(q_moat[q_moat['ticker']==i]['moatpercentage']),2) , np.round(np.mean(q_health[q_health['ticker']==i]['percentage']),2), \
            np.mean([np.round(np.mean(q_moat[q_moat['ticker']==i]['moatpercentage']),2),np.round(np.mean(q_health[q_health['ticker']==i]['percentage']),2)])])
    check_2021_q = pd.DataFrame(ls, columns=['ticker', 'moat', 'health', 'avg'])
    check_2021_q.sort_values('avg', ascending=False, inplace=True)
    full = check_2021_q.merge(weekly, on='ticker', how='inner').sort_values(by='avg', ascending=False)
    return full.drop_duplicates()

def get_scanner_y():
    # get moat
    session = Session()
    query = text(f"SELECT * from yearly_moat")
    moat = session.execute(query).fetchall()
    colnames = session.execute(query).keys()
    session.close()
    q_moat = pd.DataFrame(moat, columns=colnames).drop(columns='index')
    q_moat.replace(np.inf, np.nan, inplace=True)
    #get health
    session = Session()
    query = text(f"SELECT * from yearly_health")
    health = session.execute(query).fetchall()
    colnames = session.execute(query).keys()
    session.close()
    q_health = pd.DataFrame(health, columns=colnames).drop(columns='index')
    q_health.replace(np.inf, np.nan, inplace=True)
    #get weekly
    session = Session()
    query = text("SELECT DISTINCT ON (ticker) * FROM weekly_info ORDER BY ticker, date desc")
    weekly = session.execute(query).fetchall()
    colnames = session.execute(query).keys()
    session.close()
    weekly = pd.DataFrame(weekly, columns=colnames).drop(columns='index')
    weekly = weekly[['ticker','totalcashpershare', 'enterprisetorevenue', 'enterprisetoebitda', 'beta','longname','sector', 'industry', 'market', 'country']]
    #combine
    ls = []
    for i in q_moat[q_moat['year']==2021]['ticker']:
        ls.append([i, np.round(np.mean(q_moat[q_moat['ticker']==i]['moatpercentage']),2) , np.round(np.mean(q_health[q_health['ticker']==i]['percentage']),2), \
            np.mean([np.round(np.mean(q_moat[q_moat['ticker']==i]['moatpercentage']),2),np.round(np.mean(q_health[q_health['ticker']==i]['percentage']),2)])])
    check_2021_q = pd.DataFrame(ls, columns=['ticker', 'moat', 'health', 'avg'])
    check_2021_q.sort_values('avg', ascending=False, inplace=True)
    full = check_2021_q.merge(weekly, on='ticker', how='inner').sort_values(by='avg', ascending=False)
    return full