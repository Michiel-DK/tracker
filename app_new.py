import streamlit as st
import requests
import pandas as pd

ticker = st.text_input('ticker')

header = header = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqb2huZG9lIiwiZXhwIjoxNjcwNDg5MTc5fQ.8ooUGxJAfrio-qvhlKg4RH79gC6ISi1OPlPK8WaRoQw'}

if ticker:

    weekly = pd.DataFrame(requests.get(f"http://127.0.0.1:8000/weekly/{ticker}", headers=header).json())
    
    st.write(type(weekly))
    
    weekly.drop_duplicates(subset=weekly.columns.difference(['key', 'date']))
    
    prices = requests.get(f"http://127.0.0.1:8000/prices/{ticker}", headers=header).json()
    
    print(prices)

    st.dataframe(weekly)

    st.write(prices)