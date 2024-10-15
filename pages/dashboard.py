import streamlit as st # type: ignore


dashboard_page = st.Page("dashboard.py", title="Dashboard")
balace_page = st.Page("balance.py", title="Account Balance")
transfer_page = st.Page("transfer.py", title="Make a transfer")
logout_page = st.Page("logout.py", title="Make a transfer")

pg = st.navigation([dashboard_page, balace_page, transfer_page, logout_page])

pg.run()
