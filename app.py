import pandas as pd
import plotly.express as px
import streamlit as st

# Título de la aplicación
st.header('Análisis de anuncios de coches - reginobaby')

# Proceso de lectura de datos CSV
car_data = pd.read_csv("vehicles_us.csv")
