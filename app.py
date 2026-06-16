import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Análise de Veículos')

car_data = pd.read_csv('vehicles.csv')

hist_button = st.button('Construir histograma')

if hist_button:

    st.write('Criando histograma para price')

    fig = px.histogram(
        car_data,
        x='price'
    )

    st.plotly_chart(fig)


scatter_button = st.button('Construir gráfico de dispersão')

if scatter_button:

    st.write('Criando gráfico de dispersão para odometer e price')

    fig = px.scatter(
        car_data,
        x='odometer',
        y='price'
    )

    st.plotly_chart(fig)
