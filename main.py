import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.title('Bike Sharing Dataset Dashboard')
st.markdown('- Python libraries: numpy, pandas, streamlit, matplotlib, seaborn')
st.markdown('- Data source: https://docs.google.com/spreadsheets/d/1HoTUoAWX3jdS3WPz6chBwiEzj7BHD4uSd5Flx3bsbWE/edit?usp=sharing')

df = pd.read_excel('Assignment Data Analyst MSIB Batch 7.xlsx')
df_facebook = df[df['ga:sourceMedium'] == 'facebook / cpc']
df_google = df[df['ga:sourceMedium'] == 'google / cpc']

tab1, tab2, tab3 = st.tabs(["Peringkat Halaman", "Facebook", "Google"])

with tab1:
  option = st.selectbox(
    ("ga:users", "ga:bounceRate", "ga:pageviews", "ga:pageviewsPerSession", "ga:avgTimeOnPage"),
    placeholder="Select contact method..."
  )
  col1, col2 = st.columns(2)
  with col1:
    st.header('Facebook')
    st.table(df_facebook.groupby(by=option).agg({
    option: 'sum'
}).sort_values(by=option, ascending = False).head())
  with col2:
    st.header('Google')
    st.table(df_google.groupby(by=option).agg({
    option: 'sum'
}).sort_values(by=option, ascending = False).head())
  
