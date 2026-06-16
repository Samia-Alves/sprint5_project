import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Análise de Veículos')

car_data = pd.read_csv('vehicles.csv')

tipo = st.selectbox(
    'Escolha o tipo de veículo:',
    car_data['type'].dropna().unique()
)

car_data_filtrado = car_data[car_data['type'] == tipo]

st.write('Visualização inicial dos dados:')
st.dataframe(car_data.head())

st.write('Resumo geral:')
st.write('Total de veículos:', len(car_data))
st.write('Preço médio:', round(car_data['price'].mean(), 2))
st.write('Odômetro médio:', round(car_data['odometer'].mean(), 2))

hist_button = st.button('Construir histograma')

if hist_button:

    st.write('Criando histograma para preços')

    fig = px.histogram(
        car_data_filtrado,
        x='price'
    )

    st.plotly_chart(fig)


scatter_button = st.button('Construir gráfico de dispersão')

if scatter_button:

    st.write('Criando gráfico de dispersão para odometer e preços')

    fig = px.scatter(
        car_data_filtrado,
        x='odometer',
        y='price'
    )

    st.plotly_chart(fig)
