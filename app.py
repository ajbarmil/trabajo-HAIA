import streamlit as st
from time import sleep
import numpy as np
from genetico import AlgoritmoGenetico


def start():
    st.session_state.algoritmo = AlgoritmoGenetico()


if "algoritmo" not in st.session_state:
    st.session_state.algoritmo = None

st.title("Algoritmo genético")

if st.session_state.algoritmo is None:
    with st.form("my_form"):
        st.write("Inside the form")
        my_number = st.slider("Tamaño de la población", 1, 100)
        my_color = st.selectbox("Pick a color", ["red", "orange", "green", "blue", "violet"])
        st.form_submit_button("Submit my picks", on_click=start)
else:
    chart = st.line_chart()
    while True:
        # chart.add_rows([np.random.random()])
        chart.add_rows([st.session_state.algoritmo.iterar()])
        sleep(1)
