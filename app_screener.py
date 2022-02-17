import streamlit as st
from tracker.postgres import connect, config
import psycopg2
import pandas as pd
from tracker.frontend_functions import *

params = config(filename='/Users/michieldekoninck/code/Michiel-DK/tracker/database.ini', section='postgresql')

conn = psycopg2.connect(**params)

def app():
    col1, col2= st.columns([1,1])

    with col1:
        i = st.button('Yearly screener')
    with col2:
        c = st.button('Quarterly screener')
        
    if i:
        st.dataframe(get_scanner_y())
        
    if c:
        st.dataframe(get_scanner_q())