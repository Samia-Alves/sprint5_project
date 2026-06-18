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
st.write(
    'Average price for selected type:',
    f"${car_data_filtrado['price'].mean():,.2f}"
)
st.write('Vehicles found:', len(car_data_filtrado))

st.write('Data preview:')

tabela = car_data_filtrado.sample(5).copy()

tabela = tabela.fillna('Unknown')

st.dataframe(
    tabela.rename(columns={
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
    })
)
st.write('Summary:')
st.write(
    'Average price:',
    f"${car_data_filtrado['price'].mean():,.2f}"
)
st.write(
    'Average mileage:',
    f"{car_data_filtrado['odometer'].mean():,.0f} miles"
)

st.write('Price Distribution')

fig = px.histogram(
    car_data_filtrado,
    x='price'
)

st.plotly_chart(fig)

scatter_button = st.button('Build Scatter Plot')

if scatter_button:

    st.write('Creating scatter plot for mileage and prices')

    fig = px.scatter(
        car_data_filtrado,
        x='odometer',
        y='price'
    )

    st.plotly_chart(fig)
