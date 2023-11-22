import streamlit as st
from utils import nav_page

# Title
st.title("Caesar Cipher")

st.markdown("## Welcome to the Caesar Cipher App")

st.markdown("### A multiple algorithm encryption and decryption tool")

if st.button("Caesar Cipher"):
    nav_page("caesar_cipher")

if st.button("Atbash Cipher"):
    nav_page("atbash_cipher")

if st.button("Rot13 Cipher"):
    nav_page("rot13_cipher")

if st.button("CRot13 Cipher"):
    nav_page("crot13_cipher")

