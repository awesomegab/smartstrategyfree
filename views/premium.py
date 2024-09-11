import streamlit as st

st.title("Smart Strategy Premium")


col1, col2 = st.columns(2, gap="small", vertical_alignment="top")


with col1:
    st.title("")
    st.write("""Se você veio do Instagram mobile é necessário abrir o link no navegador padrão do dipositivo,
    toque nos três pontos no canto superior direito e selecione 'Abrir no navegador'.""")
    st.link_button("Premium", "https://smartstrategy.streamlit.app")
    st.video("https://youtu.be/0yPaWaoc0RY")


with col2:
    st.image("assets/premium advert.png")
    st.link_button("Premium", "https://smartstrategy.streamlit.app")
