from tracker.frontend_functions import *
import streamlit as st

def app():
    st.text(get_all_companies_industry('Asset Management'))
    
    st.text(get_quarterly_moat_industry('Asset Management'))