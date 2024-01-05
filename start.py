import streamlit as st
from utils import nav_page

# Title
st.title("Caesar Cipher")

st.markdown("## Welcome to the Caesar Cipher App")

st.markdown("### A multiple algorithm encryption and decryption tool")

text = st.button("Text Encryption and Decryption")
file = st.button("File Encryption and Decryption")

if text:
    nav_page("text")
if file:
    nav_page("file")