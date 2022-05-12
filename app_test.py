# -*- coding: utf-8 -*-
"""
Created on Thu May 12 16:04:21 2022

@author: Simplon
"""

import streamlit as st

st.title("Welcome to Dashboard : Score loan")

selectbox = st.sidebar.selectbox(
    "Select yes or no",
    ["Yes", "No"])

st.image('./plot/pie_plot.png')

st.write(f"You selected {selectbox}")