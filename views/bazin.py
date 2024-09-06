import yfinance as yf
import streamlit as st
import streamlit_shadcn_ui as ui


def calculadora_bazin(ticker):
    try:
        stock = yf.Ticker(ticker)
        history = stock.history(start='2019-01-01', end='2024-01-01')
        dividends = history['Dividends'].sum()
        bazin = (dividends/5)/0.06
        return bazin
    except Exception:
        return 0

st.title("Calculadora Bazin")

col1, col2 = st.columns(2, gap="medium", vertical_alignment="top")

with col1:
    st.title("")
    st.write("""**A calculadora Bazin calcula o preço justo de uma ação somando os dividendos pagos nos últimos 5 anos
     completos, excluindo o ano atual. Em seguida, divide essa soma por 5 para obter a média anual dos dividendos. O valor
      resultante é então dividido por 6%, que é a taxa mínima de retorno recomendada por Bazin. É importante ressaltar que
       esse método é uma ferramenta complementar e deve ser utilizado em conjunto com uma análise fundamentalista
        abrangente, não sendo recomendado como única base para decisões de investimento.**""")
    st.text("Selecione um país: ")
    country_selection = ui.select("País", options=["BR", "US"])

    try:
        ticker = st.text_input("Digite um ticker: ").upper()
        if country_selection == "BR" and ticker:
            ticker = ticker+".SA"
    except Exception:
        pass
    if ticker:
        try:
            bazin = calculadora_bazin(ticker)
            st.write(f"""Preço teto Bazin: **{round(bazin,2)}**""")
        except Exception:
            pass

with col2:
    st.image("assets/premium advert.png")
    st.link_button("Premium", "https://smartstrategy.streamlit.app")
