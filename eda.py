# Import libraries
import pandas as pd
import numpy as np

# Streamlit
import streamlit as st

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# # st.title
# st.title("TEST TITLE")
# st.header('INI HEADER')
# st.write('# INI WRITE')
# st.write('*INI WRITE*')

def run():
    # st title
    st.title('Exploratory Data Analysis - Weather Condition')

    # Horizontal Line
    st.write('---')

    # Input Banner
    st.image('https://timelinecovers.pro/facebook-cover/download/cr7-cristiano-ronaldo-facebook-cover.jpg')

    # Section Dataframe
    # Load Dataset
    df = pd.read_csv('weather_classification_data.csv')

    # Subheader
    st.write('## Dataset Weather Condition')

    # Show The Dataframe
    st.dataframe(df.head(10))

    # Section EDA
    # Subheader
    st.write('## Exploratory Data Analysis')

    # Title
    st.write('### Histogram Temperature')

    # Create Canvas
    fig = plt.figure(figsize=(15, 10))

    # Visualization
    sns.countplot(df, x='Temperature', hue='Temperature')

    # Show The Plot
    st.pyplot(fig)  

    # Insight
    st.write('''- Ini Point 1
            \n- Ini Point 2
            \n- Ini Point 3''')

    # Title Section
    st.write('### Data Distribution')

    # Option
    option = st.selectbox('Select Column', ('PaceTotal', 'ShootingTotal', 'PassingTotal', 'DribblingTotal', 'DefendingTotal'))

    # Visualization 2
    fig = plt.figure(figsize=(15, 10))
    sns.histplot(df['PaceTotal'], bins=20, kde=True)
    st.pyplot(fig)

    # Section Plotly
    st.write('### Relation Between Height and Weight')

    # Create Canvas
    fig = px.scatter(df, x='Height', y='Weight', hover_data=['Name', 'Age'])

    # Show Figure
    st.plotly_chart(fig)

    # Subplot
    fig, ax = plt.subplots(ncols=2, figsize=(30, 10))

    # Visualization
    sns.countplot(df, x='AttackingWorkRate', ax=ax[0])
    sns.countplot(df, x='DefensiveWorkRate', ax=ax[1])

    # Show Plot
    st.pyplot(fig)

if __name__ == '__main__':
    run()