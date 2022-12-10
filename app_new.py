import streamlit as st
import requests
import pandas as pd

all_ticks = requests.get(f"http://127.0.0.1:8000/get_all_tickers/").json()



option = st.selectbox(
        'Ticker or name?',
        all_ticks)

header = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqb2huZG9lIiwiZXhwIjoxNjcwNjg1Mjg1fQ.fo0E_MOQisHe3KWUz41O7vCpkDXbJys564q6hk8WFrk'}

if option:
    
    ticker = option['ticker']

    weekly = pd.DataFrame.from_records(requests.get(f"http://127.0.0.1:8000/weekly/{ticker}", headers=header).json())

    
    #weekly_df = weekly.drop_duplicates(subset=weekly.columns.difference(['key', 'date', 'currentprice']))
    
    st.write(weekly)
    
    quarterly = pd.DataFrame(requests.get(f"http://127.0.0.1:8000/q_financials/{ticker}", headers=header).json())
    
    st.dataframe(quarterly)
    
    yearly = pd.DataFrame(requests.get(f"http://127.0.0.1:8000/y_financials/{ticker}", headers=header).json())
    
    st.dataframe(yearly)