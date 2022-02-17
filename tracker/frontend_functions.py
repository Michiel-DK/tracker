import psycopg2
from tracker.postgres import connect, config
import pandas as pd
import numpy as np

params = config(filename='/Users/michieldekoninck/code/Michiel-DK/tracker/database.ini', section='postgresql')

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
    #cur.execute(f"""SELECT * from weekly_info WHERE (weekly_info.ticker = '{ticker}' AND (weekly_info.date = (SELECT MAX(weekly_info.date) FROM weekly_info))) GROUP BY weekly_info.date""")
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

def get_scanner_q():
    # get moat
    cur = conn.cursor()
    cur.execute('''SELECT * from quarterly_moat''')
    colnames = [desc[0] for desc in cur.description]
    moat = cur.fetchall()
    cur.close();
    q_moat = pd.DataFrame(moat, columns=colnames).drop(columns='index')
    #get health
    cur = conn.cursor()
    cur.execute('''SELECT * from quarterly_health''')
    colnames = [desc[0] for desc in cur.description]
    health = cur.fetchall()
    cur.close();
    q_health = pd.DataFrame(health, columns=colnames).drop(columns='index')
    #get weekly
    cur = conn.cursor()
    cur.execute('''SELECT * from weekly_info''')
    weekly = cur.fetchall()
    colnames = [desc[0] for desc in cur.description]
    cur.close();
    weekly = pd.DataFrame(weekly, columns=colnames).drop(columns='index')
    weekly = weekly[['ticker','totalcashpershare', 'enterprisetorevenue', 'enterprisetoebitda', 'beta','longname','sector', 'industry', 'market', 'country']]
    #combine
    ls = []
    for i in q_moat[q_moat['year']=='2021Q4']['ticker']:
        ls.append([i, np.round(np.mean(q_moat[q_moat['ticker']==i]['moatpercentage']),2) , np.round(np.mean(q_health[q_health['ticker']==i]['percentage']),2), \
            np.mean([np.round(np.mean(q_moat[q_moat['ticker']==i]['moatpercentage']),2),np.round(np.mean(q_health[q_health['ticker']==i]['percentage']),2)])])
    check_2021_q = pd.DataFrame(ls, columns=['ticker', 'moat', 'health', 'avg'])
    check_2021_q.sort_values('avg', ascending=False, inplace=True)
    full = check_2021_q.merge(weekly, on='ticker', how='inner').sort_values(by='avg', ascending=False)
    return full.drop_duplicates()

def get_scanner_y():
    # get moat
    cur = conn.cursor()
    cur.execute('''SELECT * from yearly_moat''')
    colnames = [desc[0] for desc in cur.description]
    moat = cur.fetchall()
    cur.close();
    q_moat = pd.DataFrame(moat, columns=colnames).drop(columns='index')
    #get health
    cur = conn.cursor()
    cur.execute('''SELECT * from yearly_health''')
    colnames = [desc[0] for desc in cur.description]
    health = cur.fetchall()
    cur.close();
    q_health = pd.DataFrame(health, columns=colnames).drop(columns='index')
    #get weekly
    cur = conn.cursor()
    cur.execute(f"""SELECT * from weekly_info""")
    weekly = cur.fetchall()
    colnames = [desc[0] for desc in cur.description]
    cur.close();
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