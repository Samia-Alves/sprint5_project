import pandas as pd
import plotly.express as px
import streamlit as st

st.title('🚗 Análise de Veículos')

car_data = pd.read_csv('vehicles.csv')
car_data['is_4wd'] = car_data['is_4wd'].map({
    1.0: 'Sim'
}).fillna('Não informado')

tipo = st.selectbox(
    'Escolha o tipo de veículo:',
    car_data['type'].dropna().unique()
)

car_data_filtrado = car_data[car_data['type'] == tipo]
st.write('Preço filtrado:', f"{car_data_filtrado['price'].mean():.2f}")
st.write('Veículos encontrados:', len(car_data_filtrado))

st.write('Visualização inicial dos dados:')
st.dataframe(car_data_filtrado.sample(5))

st.write('Resumo geral:')
st.write('Preço médio:', f"{car_data_filtrado['price'].mean():.2f}")
st.write('Odômetro médio:', f"{car_data_filtrado['odometer'].mean():.0f}")

st.write('Distribuição dos preços')

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
