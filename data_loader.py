import pandas as pd
import streamlit as st


@st.cache_data
def load_data():
    file_path = "data/Sample_Superstore.xls"
    return pd.read_excel(file_path)