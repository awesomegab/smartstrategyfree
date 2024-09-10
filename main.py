import streamlit as st

# Esconder o ícone do GitHub
hide_github_icon = """
    <style>
    .stApp > header {visibility: hidden;}
    </style>
"""
st.markdown(hide_github_icon, unsafe_allow_html=True)

st.image("assets/top banner.png")

bazin_page = st.Page(
    page="views/bazin.py",
    title="Calculadora Graham",
    icon=":material/chevron_right:",
    default=True
)
premium_page = st.Page(
    page = "views/premium.py",
    title="Smart Strategy Premium",
    icon=":material/workspace_premium:"
)
contato_page = st.Page(
    page= "views/contato.py",
    title="Entre em contato",
    icon=":material/contact_support:"
)
privacidade_page = st.Page(
    page="views/privacidade.py",
    title="Política de Privacidade",
    icon=":material/policy:"
)

pg = st.navigation({"Ferramentas":[bazin_page],"Smart Strategy Premium":[premium_page],"Outro":[contato_page, privacidade_page]})

st.logo("assets/logo.png")

st.sidebar.text("Smart Strategy")

pg.run()


