import streamlit as st
from trilio import *
import requests
import Trilio_Blockchain_Mian as tbm # importing main page

# importing variables from main
all_wallets = tbm.all_wallets

# header section
st.subheader("This is a blockchain app build with streamlit")
# st_lottie(lotte_ethereum, height=500, key="ethereum")
with st.container():
    # left_column, right_column = st.columns(2)
    # with left_column:
    # title
    st.title("blockchain transaction database")
# with right_column:
#     st_lottie(lotte_ethereum, height=150, key="ethereum")
# header
st.header("Blockchain ")
# name = st.text_input("enter the name of your block", )
# data = name

with st.container():
    bc = Trilio()

# Wallet creation
    st.markdown("***")
    if st.button("press to create wallet"):
        wallet = bc.Wallet.create_wallet()
        st.success(wallet)
        all_wallets.append(wallet)

st.text(all_wallets)