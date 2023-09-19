import streamlit as st
import database as db
import pandas as pd

st.set_page_config(
    page_title= "PepMine App",
    page_icon="⛏",
)

st.title("Get more Tokens!")
if "get_input" not in st.session_state:
    st.session_state["get_input"] = 0
get_input = st.text_input("Input the token you want to get here", st.session_state["get_input"])
# print(get_input)
if float(get_input) >0:
    st.session_state["get_input"] = get_input
    # print("AHA")
    money_get = float(st.session_state["get_input"])
    st.write("Paying...")
    st.write(f"You get {money_get}!")
    st.session_state["user_token"] = st.session_state["user_token"]+money_get
    db.update_user(st.session_state["user_key"],{"token":st.session_state["user_token"]})



else:
    st.write("trade fail!")