import streamlit as st # type: ignore

home_page = st.Page("app.py", title="Home")
login_page = st.Page("pages/login.py", title="Login")
pg = st.navigation([home_page, login_page])

pg.run()
