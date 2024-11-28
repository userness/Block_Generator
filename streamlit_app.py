import streamlit as st


hello = open("hello.md", "r")
hello = hello.read()

st.markdown(hello)

st.divider()

st.link_button("Go to downloads", "pages/Downloads.py")
st.link_button("Go to the generator", "pages/Generator.py")