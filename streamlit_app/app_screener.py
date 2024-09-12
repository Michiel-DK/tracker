import streamlit as st
import pandas as pd
from tracker.frontend_functions import *

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