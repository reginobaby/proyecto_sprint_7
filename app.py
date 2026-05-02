import pandas as pd
import plotly.express as px
import streamlit as st

# Título de la aplicación
st.header('Análisis de anuncios de coches - reginobaby')

# Proceso de lectura de datos CSV
car_data = pd.read_csv("vehicles_us.csv")

# Crear boton para el histograma
hist_button = st.button("construir histograma")

if hist_button:  # comando que se usa cuando hacen click al boton
    st.write(
        "Creación de un histograma para el conjunto de datos de anuncios de venta de coches")

# creación de histograma
fig = px.histogram(car_data, x="odometer")

# codigo que muestra el grafico plotly interactivo
st.plotly_chart(fig, use_container_width=True)

# Boton para grafico de disperción
scatter_button = st.button("Construir gráfico de dispersión")

# Creación de grafico de disperción
fig_scatter = px.scatter(car_data, x="odometer", y="price")

# mostrar el gráfico
st.plotly_chart(fig_scatter, use_container_width=True)
