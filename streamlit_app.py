import streamlit as st

st.page_link("streamlit_app.py", label="Home", icon="🏠")



hello = open("hello.md", "r")
hello = hello.read()

st.markdown(hello)

st.divider()

st.link_button("Go to downloads", "pages/downloads.py")
st.link_button("Go to the generator", "pages/gen.py")