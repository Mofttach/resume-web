import streamlit as st

# SETUP
aboutpage = st.Page(
    page="views/aboutme.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)
project1 = st.Page(
    page="views/chatbot.py",
    title="Chatbot",
    icon=":material/smart_toy:",
)

# NAVIGASI
pg = st.navigation(
    {
        "Info": [aboutpage],
        "Projects": [project1]
    }
)

# perlogoan
st.logo("assets/mofttachlogo.png", size='large')
st.sidebar.text("Copyrigth punya Fttach")

pg.run()