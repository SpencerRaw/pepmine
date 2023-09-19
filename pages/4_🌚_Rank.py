import streamlit as st
import database as db
import pandas as pd

st.set_page_config(
    page_title= "PepMine App",
    page_icon="⛏",
)

st.title("Crowdfunding Rank!")

peps = db.fetch_all_peps()

sequences = [pep["key"] for pep in peps]
funds = [pep["fund_now"] for pep in peps]

data_list = [(sequences[i], funds[i]) for i in range(len(funds))]

df = pd.DataFrame(data_list, columns=['Peptide_Sequence', 'sum']).sort_values(by='sum', ascending=False).query('sum != 0').reset_index(drop=True)
df.index = df.index + 1


st.table(df)