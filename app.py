# -*- coding: utf-8 -*-
"""
Created on Wed May 11 10:05:45 2022

@author: Simplon
"""


import streamlit as st

st.title("Welcome to Dashboard : Score loan")
st.write("Visualisation des données sur l'ensemble du dataset")

st.image('./plot/pie_plot.png')






selectbox = st.sidebar.selectbox(
    "Select Customers ID",
    ["Yes", "No"]
)

st.write(f"You selected {selectbox}")