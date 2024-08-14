import streamlit as st
import pandas as pd
import plotly_express as px

vehicles_data = pd.read_csv(r"C:\Users\andyt\OneDrive\Escritorio\PROYECTOS\Sprint_6_Project\vehicles_us.csv")

hist_button = st.button("Construir histograma")

st.header("Kilómetros recorridos por modelo de carro")

if hist_button:
    st.write("Creación de un histograma para el conjunto de datos de carros")

    fig_1 = px.histogram(vehicles_data, x="odometer")

    st.plotly_chart(fig_1, use_container_width=True)
    
    fig_1.show()

disp_button = st.button("Relación entre precio y kilómetros")

st.header("Relación entre precio y kilómetros ")

if disp_button:
    st.write("Creación de un gráfico de dispersión para el conjunto de datos de carros")

    fig_2 = px.scatter(vehicles_data, x="odometer", y="price")

    st.plotly_chart(fig_2, use_container_width=True)
    
    fig_2.show()