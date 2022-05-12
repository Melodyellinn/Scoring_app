# -*- coding: utf-8 -*-
"""
Created on Wed May 11 10:05:45 2022

@author: Simplon
"""

#import os
import streamlit as st


st.image('./pie_plot.png')




#MODEL_DIR = os.path.join(os.path.dirname('__file__'), 'model.pkl')
#if not os.path.isdir(MODEL_DIR):
#    os.system('runipy notebook_model.ipynb')

#model = pickle.load(open("model.pkl","rb"))
#model = load_model('model.pkl')

st.title("Welcome to Dashboard : Score loan")

selectbox = st.sidebar.selectbox(
    "Select Customers ID",
    ["Yes", "No"]
)

st.write(f"You selected {selectbox}")