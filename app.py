import streamlit as st
from tracker.postgres import connect, config
import psycopg2
import pandas as pd
from tracker.frontend_functions import *

params = config(filename='/Users/admin/code/Michiel-DK/tracker/database.ini', section='postgresql')

conn = psycopg2.connect(**params)
		
# create a cursor for tickers
cur = conn.cursor()
cur.execute('''SELECT shortname, ticker from weekly_info''')
all_tickers = cur.fetchall()
cur.close();


option = st.selectbox(
     'Ticker or name?',
     all_tickers)

col1, col2, col3, col4 = st.columns([1,1,1,1])

with col1:
    i = st.button('Company info')
with col2:
    c = st.button('Current data')
with col3:
    q = st.button('Quarterly')
with col4:
    y = st.button('Yearly')

if option:
    if (i and option):
        weekly = get_weekly(option[1])
        st.header(weekly.to_dict('records')[0]['longname'])
        st.table(weekly[['sector', 'industry', 'market', 'marketcap', 'enterprisevalue']])
        st.write(weekly.to_dict('records')[0]['longbusinesssummary'])
        
    if (q and option):
        st.header("Quarterly Moat")
        st.table(get_quarterly_moat(option[1]))
        
        st.header("Quarterly Health")
        st.table(get_quarterly_health(option[1]))
        
    if (y and option):
        st.header("Yearly Moat")
        st.table(get_yearly_moat(option[1]))
        
        st.header("Yearly Health")
        st.table(get_yearly_health(option[1]))
    
    