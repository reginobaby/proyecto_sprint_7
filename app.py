import pandas as pd
import plotly_express as px
import streamlit as st

# Configuración de la pestaña (Nombre e Icono)
st.set_page_config(
    page_title="Análisis de Vehículos - reginobaby", page_icon="🚗", layout="wide")

# Título con estilo
st.write("# 🏎️ Dashboard de Análisis de Vehículos")
st.markdown(f"**Usuario:** reginobaby | **Proyecto:** Sprint 7")
st.markdown("---")

# Carga de datos
car_data = pd.read_csv('vehicles_us.csv')

# Crear dos columnas para organizar las casillas y gráficas
col1, col2 = st.columns(2)

with col1:
    st.write("### Histograma")
    # Casilla de verificación para el histograma
    build_histogram = st.checkbox('Mostrar Histograma de Kilometraje')

    if build_histogram:
        st.write('Distribución de la columna odometer')
        fig = px.histogram(car_data, x="odometer",
                           color_discrete_sequence=['#00CC96'])
        st.plotly_chart(fig, use_container_width=True)

with col2:
    st.write("### Gráfico de Dispersión")
    # Casilla de verificación para el gráfico de dispersión
    build_scatter = st.checkbox('Mostrar Gráfico de Dispersión (Precio vs Km)')

    if build_scatter:
        st.write('Relación entre kilometraje y precio de venta')
        fig_scatter = px.scatter(
            car_data, x="odometer", y="price", opacity=0.4)
        st.plotly_chart(fig_scatter, use_container_width=True)
