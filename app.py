# -*- coding: utf-8 -*-
"""
Created on Wed May 11 10:05:45 2022

@author: Simplon
"""


import streamlit as st

st.title("Welcome to Dashboard : Score loan")
st.write("Visualisation des données sur l'ensemble du dataset")

st.write("Distribution des variables")

st.image('./plot/distrib.png')

st.write("Répartition de la target")

st.image('./plot/target_01.png') 
st.image('./plot/target_02.png')
st.image('./plot/target_03.png')

st.image('./plot/pie_plot.png')

