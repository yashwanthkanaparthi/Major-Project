import streamlit as st

number = st.slider("Pick a number", 0, 100)

st.write(number)