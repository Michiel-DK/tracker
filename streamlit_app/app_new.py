import streamlit as st
import requests
import pandas as pd
from tracker.update_quarterly import update_specific_ticker

all_ticks = requests.get(f"http://127.0.0.1:8000/get_all_tickers/").json()



option = st.selectbox(
        'Ticker or name?',
        all_ticks)

header = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqb2huZG9lIiwiZXhwIjoxNjc1MTYyNTMwfQ.QFAf5_s5-gEaax6-c8rPiG0CtnEer36EMDzfS25EAGE'}

if option:
        ticker = option['ticker']
        
        if st.button('update quarterly_financials'):
                st.write(f'updating ticker {ticker}')
                update_specific_ticker(ticker)
    
    

        weekly = pd.DataFrame.from_records(requests.get(f"http://127.0.0.1:8000/weekly/{ticker}", headers=header).json())

        
        #weekly_df = weekly.drop_duplicates(subset=weekly.columns.difference(['key', 'date', 'currentprice']))
        
        st.write(weekly)
        
        quarterly = pd.DataFrame(requests.get(f"http://127.0.0.1:8000/q_financials/{ticker}", headers=header).json())
        
        st.dataframe(quarterly)
        
        yearly = pd.DataFrame(requests.get(f"http://127.0.0.1:8000/y_financials/{ticker}", headers=header).json())
        
        st.dataframe(yearly)
    