import streamlit as st
import pandas as pd
from tracker.frontend_functions import *

		
# create a cursor for tickers

def app():
    option = st.selectbox(
        'Ticker or name?',
        get_all_tickers())

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
        
        weekly = get_weekly(option[0])
        weekly_comp = weekly[0]
        name = weekly_comp['industry'][0]
        st.header(weekly_comp.to_dict('records')[0]['longname'])
        if (i and option):
            #weekly_comp = weekly[0]
            #st.header(weekly.to_dict('records')[0]['longname'])
            st.table(weekly_comp[['sector', 'industry', 'market', 'marketcap', 'enterprisevalue']])
            st.write(weekly_comp.to_dict('records')[0]['longbusinesssummary'])
            
        if (c and option):
            weekly_value = weekly[1]
            st.table((weekly[1].T).join(get_avg_weekly_industry(name), how='left'))
            st.table(weekly[2].T)
            st.table(weekly[3].T)
            st.table(weekly[4])
            
        if (q and option):
            st.header("Quarterly Moat")
            st.table(get_quarterly_moat(option[0]))
            
            st.header("Quarterly Health")
            st.table(get_quarterly_health(option[0]))
            
        if (y and option):
            st.header("Yearly Moat")
            st.table(get_yearly_moat(option[0]))
            
            st.header("Yearly Health")
            st.table(get_yearly_health(option[0]))
            
    
    