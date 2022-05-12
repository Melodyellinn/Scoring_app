# -*- coding: utf-8 -*-
"""
Created on Wed May 11 10:05:45 2022

@author: Simplon
"""

import streamlit as st



st.title("Welcome to Streamlit!")

selectbox = st.sidebar.selectbox(
    "Select yes or no",
    ["Yes", "No"]
)

st.write(f"You selected {selectbox}")