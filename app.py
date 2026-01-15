import streamlit as st
import pandas as pd

st.title("📊 Любими неща – класна анкета")

# Инициализация на данните
if "uchenici" not in st.session_state:
    st.session_state.uchenici = {
        "Иванка": 0,
        "Никол": 0,
        "Ивайло": 0,
        "Алекс": 0
    }

if "ucenki" not in st.session_state:
    st.session_state.ucenki = {
        "6": 0,
        "5": 0,
        "4": 0,
        "3": 0,
        "2": 0
    }

st.subheader("Избери ученик и оценка")

uchenik = st.selectbox("Ученик:", list(st.session_state.uchenici.keys()))
ucenki = st.selectbox("Оценка:", list(st.session_state.ucenki.keys()))

if st.button("Запази избора"):
    st.session_state.uchenici[uchenik] += 1
    st.session_state.ucenki[ucenki] += 1
    st.success("Изборът е записан!")

st.divider()

st.subheader("📈 Резултати")

# Графика за цветовете
st.write("Ученици")
uchenici_df = pd.DataFrame.from_dict(
    st.session_state.uchenici, orient="index", columns=["Брой"]
)
st.bar_chart(uchenici_df)

# Графика за спортовете
st.write("Оценки")
ucenki_df = pd.DataFrame.from_dict(
    st.session_state.ucenki, orient="index", columns=["Брой"]
)
st.bar_chart(ucenki_df)
