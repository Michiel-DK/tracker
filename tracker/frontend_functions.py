from tracker.postgres import connect, config
import pandas as pd
import numpy as np
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import dotenv

#params = config(filename='/Users/michieldekoninck/code/Michiel-DK/tracker/database.ini', section='postgresql')

#conn = psycopg2.connect(**params)

from dotenv import dotenv_values

database_env = dotenv_values("database.env")

engine = create_engine(f"postgresql://{database_env['POSTGRES_USER']}:{database_env['POSTGRES_PASSWORD']}@localhost:{database_env['POSTGRES_PORT']}/{database_env['POSTGRES_DB']}")
Session = sessionmaker(bind=engine)

def get_all_tickers():
    session = Session()
    query = text(f"SELECT shortname, ticker from weekly_info ORDER BY ticker")
    all_ticks = session.execute(query).fetchall()
    #colnames = session.execute(query).keys()
    session.close()
    return all_ticks
    

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
    return selected_health_df

def get_weekly(ticker):
    session = Session()
    query = text(f"SELECT * from weekly_info WHERE ticker = '{ticker}'")
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

def get_scanner_q():
    # get moat
    session = Session()
    query = text(f"SELECT * from quarterly_moat")
    moat = session.execute(query).fetchall()
    colnames = session.execute(query).keys()
    session.close()
    q_moat = pd.DataFrame(moat, columns=colnames).drop(columns='index')
    #get health
    session = Session()
    query = text(f"SELECT * from quarterly_health")
    health = session.execute(query).fetchall()
    colnames = session.execute(query).keys()
    session.close()
    q_health = pd.DataFrame(health, columns=colnames).drop(columns='index')
    #get weekly
    session = Session()
    query = text(f"SELECT * from weekly_info")
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
    #get health
    session = Session()
    query = text(f"SELECT * from yearly_health")
    health = session.execute(query).fetchall()
    colnames = session.execute(query).keys()
    session.close()
    q_health = pd.DataFrame(health, columns=colnames).drop(columns='index')
    #get weekly
    session = Session()
    query = text(f"SELECT * from weekly_info")
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