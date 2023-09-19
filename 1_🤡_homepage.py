import streamlit as st

import streamlit_authenticator as stauth

import database as db
import pandas as pd



st.set_page_config(
    page_title= "PepMine App",
    page_icon="⛏",
)

# 等等...
users = db.fetch_all_users()
usernames = [user["key"] for user in users]
names = [user["name"] for user in users]
tokens = [user["token"] for user in users]
pep_nfts = [user["pep_nft"] for user in users]
hashed_passwords = [user["password"] for user in users]

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,"pepmine_dashboard", "abcdef", cookie_expiry_days=1)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:

    # 路由和导航
    
    # st.sidebar.title(f"Welcome {name}")
    
    # 等等...

    # st.title(f"Welcome {name}")
    
    st.title(f"Welcome {name}")
    # print(users)
    id_ = names.index(name)
    st.session_state["user_key"] = usernames[id_]
    st.session_state["user_id"] = id_
    st.session_state["user_token"] = tokens[id_]
    st.session_state["pep_nft"] = pep_nfts[id_]
    token_num = st.session_state["user_token"]
    st.subheader(f"You have {token_num} tokens")

    
    your_nft = pep_nfts[id_]
    if len(your_nft) == 0:
        st.subheader("You don't have any Investments")
    else:
        st.subheader("Your Investments")
        # 将字典转换为元组列表
        data_list = [(key, value) for key, value in your_nft.items()]

        # 创建DataFrame
        df = pd.DataFrame(data_list, columns=['Peptide Sequence', 'Your Invest'])

        # investment_df = pd.DataFrame(your_nft)
        st.table(df)
    st.sidebar.success("Select a page above")
    authenticator.logout("Logout", "sidebar")
    

