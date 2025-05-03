import streamlit as st
from time import sleep
import numpy as np
from genetico import AlgoritmoGenetico, Hiperparametros


def start():
    st.session_state.algoritmo = AlgoritmoGenetico(st.session_state.hiperparametros)


if "algoritmo" not in st.session_state:
    st.session_state.algoritmo = None

st.title("Algoritmo genético")

if st.session_state.algoritmo is None:
    with st.form("my_form"):
        # st.write("Inside the form")
        default = Hiperparametros()
        partidas = st.slider("Número de partidas para las simulaciones", 1, 20, value=default.partidas)
        tamaño = st.slider("Tamaño de la población", 1, 100, value=default.tamaño)
        mutate_prob = st.slider("Probabiliad de mutación", 0.0, 1.0, value=default.mutate_prob)
        mutate_var = st.slider("Variabilidad de la mutación", 0.0, 1.0, value=default.mutate_var)
        seleccion_m = st.slider("Valor *m* para la selección", 1, 100, value=default.seleccion_m)
        seleccion_n = st.slider("Valor *n* para la selección", 1, 100, value=default.seleccion_n)

        st.session_state.hiperparametros = Hiperparametros(
            partidas=partidas,
            tamaño=tamaño,
            mutate_prob=mutate_prob,
            mutate_var=mutate_var,
            seleccion_m=seleccion_m,
            seleccion_n=seleccion_n,
        )

        st.form_submit_button("Iniciar algoritmo", on_click=start)
else:
    chart = st.line_chart()
    print(len(st.session_state.algoritmo.poblacion))
    while True:
        # chart.add_rows([np.random.random()])
        chart.add_rows([st.session_state.algoritmo.iterar()])
        sleep(1)
