# Import Libraries
import streamlit as st
import eda
import prediction

# Navigation
navigation = st.sidebar.selectbox('Pilih Halaman', ['EDA', 'Predictor'])

# Page
if navigation == 'Predictor':
    prediction.run()
else : 
    eda.run()