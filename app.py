import app_company
import app_screener
import streamlit as st
PAGES = {
    "Company": app_company,
    "Screener": app_screener
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()