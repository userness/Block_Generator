import streamlit as st

st.navigation([disabled])

hello = open("hello.md", "r")
hello = hello.read()

st.markdown(hello)

st.divider()

col1, col2 = st.columns(2)

# Add buttons in separate columns to place them side by side
with col1:
    st.page_link("pages/Downloads.py", label="To Downloads", icon="⬇️")
with col2:
    st.page_link("pages/Generator.py", label="To The Generator", icon="⚙️")