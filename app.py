import pandas as pd
import plotly.express as px
import streamlit as st

st.title('🚗 Vehicle Analysis')

car_data = pd.read_csv('vehicles.csv')
car_data['is_4wd'] = car_data['is_4wd'].map({
    1.0: 'Yes'
}).fillna('Unknown')

tipo = st.selectbox(
    'Choose a vehicle type:',
    car_data['type'].dropna().unique()
)

car_data_filtrado = car_data[car_data['type'] == tipo]
st.write('Filtered price:', f"{car_data_filtrado['price'].mean():.2f}")
st.write('Vehicles found:', len(car_data_filtrado))

st.write('Data preview:')


sst.dataframe(
    car_data_filtrado.rename(columns={
        'price': 'Price',
        'model_year': 'Year',
        'model': 'Model',
        'type': 'Type',
        'date_posted': 'Date Posted',
        'days_listed': 'Days Listed',
        'odometer': 'Mileage',
        'condition': 'Condition',
        'cylinders': 'Cylinders',
        'fuel': 'Fuel',
        'transmission': 'Transmission',
        'paint_color': 'Color',
        'is_4wd': '4WD'
    }).fillna('Unknown').sample(5)
)
st.write('Summary:')
st.write('Average price:', f"{car_data_filtrado['price'].mean():.2f}")
st.write('Average mileage:', f"{car_data_filtrado['odometer'].mean():.0f}")

st.write('Price Distribution')

fig = px.histogram(
    car_data_filtrado,
    x='price'
)

st.plotly_chart(fig)

scatter_button = st.button('Build Scatter Plot')

if scatter_button:

    st.write('Criando gráfico de dispersão para odometer e preços')

    fig = px.scatter(
        car_data_filtrado,
        x='odometer',
        y='price'
    )

    st.plotly_chart(fig)
