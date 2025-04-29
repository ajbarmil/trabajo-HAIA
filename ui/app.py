import streamlit as st
from time import sleep
import numpy as np


def start():
    st.session_state.running = True


if "running" not in st.session_state:
    st.session_state.running = False

st.title("Algoritmo genético")

if not st.session_state.running:
    with st.form("my_form"):
        st.write("Inside the form")
        my_number = st.slider("Tamaño de la población", 1, 100)
        my_color = st.selectbox("Pick a color", ["red", "orange", "green", "blue", "violet"])
        st.form_submit_button("Submit my picks", on_click=start)
else:
    chart = st.line_chart()
    while True:
        chart.add_rows([np.random.random()])
        sleep(1)
