import streamlit as st
import database as db
import pandas as pd

st.set_page_config(
    page_title= "PepMine App",
    page_icon="⛏",
)

st.title("Once download, you get payed!")
@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

csv = convert_df(pd.read_csv('grampa.csv'))


st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name="pepmind_data.csv",
    mime='text/csv',
)