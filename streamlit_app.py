import streamlit as st


hello = open("hello.md", "r")
hello = hello.read()

st.markdown(hello)

st.divider()

col1, col2 = st.columns(2)

# Add buttons in separate columns to place them side by side
with col1:
    st.link_button("Go to downloads", "pages/Downloads.py")
with col2:
    st.link_button("Go to the generator", "pages/Generator.py")