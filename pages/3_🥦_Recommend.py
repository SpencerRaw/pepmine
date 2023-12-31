import streamlit as st
import database as db

st.set_page_config(
    page_title= "PepMine App",
    page_icon="⛏",
)

# peps = db.fetch_all_peps()
# sequences = [pep["key"] for pep in peps]


st.title("Don't know what to fund? Try it!")

if "our_input" not in st.session_state:
    st.session_state["our_input"] = ""

my_input = st.text_input("What property are you interested in?", st.session_state["our_input"])
# submit = st.button("Submit")
if my_input:
    st.session_state["our_input"] = "AABBC"
    search_result =db.get_pep("AABBC")
    # print(search_result)
    if search_result:
        st.write(f"Based on your interest, we recommend you to fund AABBC!")
        percentle = search_result["fund_now"]/search_result["fund_target"]*100
        st.write(f"{my_input}: {percentle}%")
        st.session_state["pep"] = "AABBC"
        st.session_state["fund_now"] = search_result["fund_now"]
        st.session_state["fund_target"] = search_result["fund_target"]

        if "pay_input" not in st.session_state:
            st.session_state["pay_input"] = 0
        pay_input = st.text_input("Input the token you want to pay here", st.session_state["pay_input"])
        # submit_pay = st.button("Pay")

        if pay_input:
            # print("AHA")
            st.session_state["pay_input"] = pay_input
            if float(st.session_state["pay_input"]) >0 and float(st.session_state["pay_input"]) < st.session_state["user_token"]:
                money_pay = float(st.session_state["pay_input"])
                st.write(f"You pay {money_pay}!")
                st.session_state["user_token"] = st.session_state["user_token"]-money_pay
                db.update_user(st.session_state["user_key"],{"token":st.session_state["user_token"]})
                user_dict_now = st.session_state["pep_nft"]
                if user_dict_now.get(st.session_state["pep"]) is not None:
                    user_dict_now[st.session_state["pep"]]+=money_pay
                else:
                    user_dict_now[st.session_state["pep"]] = money_pay
                db.update_user(st.session_state["user_key"],{"pep_nft":user_dict_now})
                pep_fund_now = st.session_state["fund_now"]+money_pay
                db.update_pep(st.session_state["pep"],{"fund_now":pep_fund_now})



            else:
                st.write("Fund fail!")

        



    else:
        st.write("This peptide have been researched!")

