import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv("educacion.csv")

st.title("Análisis de Datos de Educación en Colombia")

# Subir el archivo
uploaded_file = st.file_uploader("Cargar archivo 'educacion.csv'", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.dataframe(df)

# Filtros en la barra lateral
st.sidebar.header("Filtros")
nivel_educativo = st.sidebar.multiselect(
    "Nivel educativo", df["Nivel educativo"].unique()
)
carrera = st.sidebar.multiselect("Carrera", df["Carrera"].unique())
institucion = st.sidebar.multiselect("Institución", df["Institución"].unique())

# Aplicar filtros
df_filtrado = df.copy()
if nivel_educativo:
    df_filtrado = df_filtrado[df_filtrado["Nivel educativo"].isin(nivel_educativo)]
if carrera:
    df_filtrado = df_filtrado[df_filtrado["Carrera"].isin(carrera)]
if institucion:
    df_filtrado = df_filtrado[df_filtrado["Institución"].isin(institucion)]

st.dataframe(df_filtrado)

# Estadísticas descriptivas
st.subheader("Estadísticas Descriptivas")
st.write(df_filtrado.describe())

# Conteo de estudiantes por nivel educativo
st.subheader("Conteo de Estudiantes por Nivel Educativo")
st.bar_chart(df_filtrado["Nivel educativo"].value_counts())

# Distribución de la Edad
st.subheader("Distribución de la Edad")
fig, ax = plt.subplots()
ax.hist(df_filtrado["Edad"], bins=10, edgecolor="black")
ax.set_xlabel("Edad")
ax.set_ylabel("Frecuencia")
ax.set_title("Distribución de Edad")
st.pyplot(fig)
