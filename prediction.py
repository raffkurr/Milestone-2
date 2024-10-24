# Import Libraries
import pandas as pd
import numpy as np
import streamlit as st

# Pickle
import pickle as pkl

# Load Model
with open('model_v1.pkl', 'rb') as file_1:
    model = pkl.load(file_1)

def run():
    # Title
    st.title('Today Weather Condition Prediction')

    # Horizontal Line
    st.write('---')

    # Upload Image
    st.image('https://www.thehomepagenetwork.com/wp-content/uploads/2022/01/Banner-Weather.jpg')

    # Description
    st.write('''This page will allow user to predict the weather condition based on their data''')

    # Form
    with st.form(key= 'form parameter'):
        Temperature = st.number_input('Temperature', min_value=0, max_value=50, step=1) 
        Humadity = st.number_input('Humadity', min_value=0, max_value=100, step=1)
        Wind_Speed = st.number_input('Wind Speed', min_value=0, max_value=100, step=1)
        Precipitation = st.number_input('Precipitation', min_value=0, max_value=100, step=1)
        Cloud_Cover = st.number_input('Cloud Cover', min_value=0, max_value=100, step=1)
        Atmospheric_Pressure = st.number_input('Atmospheric Pressure', min_value=0, max_value=100, step=1)
        UV_Index = st.number_input('UV Index', min_value=0, max_value=100, step=1)
        Season = st.number_input('Season', min_value=0, max_value=100, step=1)
        Visibility = st.number_input('Visibility', min_value=0, max_value=100, step=1)
        Location = st.number_input('Location', min_value=0, max_value=100, step=1)

        submit = st.form_submit_button('Predict')

    # Data Inference
    df = pd.DataFrame([{
        'Temperature':[Temperature],
        'Humadity' : [Humadity],
        'Wind_Speed' : [Wind_Speed],
        'Precipitation' : [Precipitation],
        'Cloud_Cover' : [Cloud_Cover],
        'Atmospheric_Pressure' : [Atmospheric_Pressure],
        'UV_Index' : [UV_Index],
        'Season' : [Season],
        'Visibility' : [Visibility],
        'Location' : [Location]}])

    # Show Data (Optional)
    st.dataframe(df)

    # Predict
    if submit:
        y_pred = model.predict(df)
        st.write(f'### Weather Condition {Temperature} : {y_pred[0]:.2f}')

if __name__ == '__main__':
    run()