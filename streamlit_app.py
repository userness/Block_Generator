import streamlit as st

hello = open("hello.md", "r")
hello = hello.read()

st.markdown(hello)