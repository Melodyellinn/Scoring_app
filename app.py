# -*- coding: utf-8 -*-
"""
Created on Wed May 11 10:05:45 2022

@author: Simplon
"""

import pandas as pd
import os
import os.path
import pickle
import streamlit as st
from sklearn.model_selection import train_test_split

path = os.path.join(os.getcwd(), r'data\application_train_light.csv').replace("\\",'/')
# print(path, 'BLOOOOOOOOOOOOOP')
df = pd.read_csv(path)

MODEL_DIR = os.path.join(os.getcwd(), r'model.pkl').replace("\\",'/')
# print(MODEL_DIR, 'BLAAAAAAAAAP')
with open(MODEL_DIR , 'rb') as handle:
    model = pickle.load(handle)

###### DROP MISSING VALUES ######
df.dropna(inplace=True)
###### DEFINE X y AND SPLIT TRAIN/TEST ######
X = df.drop('TARGET', axis=1)
y = df['TARGET']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.25, random_state=42)
###### SEPARATE TYPE COLUMNS ######
categorials = list(X_train.select_dtypes('object').columns)
numericals = list(X_train.select_dtypes(exclude=['object']).columns)

if st.button('Predict'):
    val = model.predict(X_test)
#    val_1 = pd.DataFrame(data=val)
    st.write(val)


st.title("Welcome to Dashboard")
st.write("Visualisation des données sur l'ensemble du dataset")

st.write("Distribution des variables")

st.image('./plot/distrib.png')

st.write("Répartition de la target")

st.image('./plot/target_01.png') 
st.image('./plot/target_02.png')
st.image('./plot/target_03.png')

st.image('./plot/pie_plot.png')