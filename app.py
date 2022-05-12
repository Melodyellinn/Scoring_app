# -*- coding: utf-8 -*-
"""
Created on Wed May 11 10:05:45 2022

@author: Simplon
"""

import pickle
import pandas as pd
import streamlit as st

model = pickle.load(open("model.pkl","rb"))

features = pd.DataFrame(
    model.data, columns= model.feature_names
)
#target = pd.Series(model.TARGET)

st.title("Welcome to Dashboard : Score loan")

selectbox = st.sidebar.selectbox(
    "Select Customers ID",
    ["model.['SK_ID_CURR'][0]"]
)

st.write(f"You selected {selectbox}")