import streamlit as st

st.title("Smart Strategy Premium")


col1, col2 = st.columns(2, gap="small", vertical_alignment="top")


with col1:
    st.link_button("Premium", "https://smartstrategy.streamlit.app")
    st.video("https://youtu.be/0yPaWaoc0RY")
    st.link_button("Premium", "https://smartstrategy.streamlit.app")

with col2:
    st.title("")
    st.image("assets/premium advert.png")
    st.link_button("Premium", "https://smartstrategy.streamlit.app")
