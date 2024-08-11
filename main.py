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

tab1, tab2 = st.tabs(["Facebook", "Google"])
with tab1:
      st.header('Halaman dengan jumlah pengguna tertinggi')
      st.table(data=df_facebook.groupby(by='ga:pageTitle').agg({
            'ga:users': 'sum'
        }).sort_values(by='ga:users', ascending = False).head())
      
      st.header('Halaman dengan jumlah bounce rate tertinggi')
      st.table(df_facebook.groupby(by='ga:pageTitle').agg({
          'ga:pageviews': 'sum'
      }).sort_values(by='ga:pageviews', ascending = False).head())
      
      st.header('Halaman dengan jumlah pembaca halaman tertinggi')
      st.table(df_facebook.groupby(by='ga:pageTitle').agg({
          'ga:pageviews': 'sum'
      }).sort_values(by='ga:pageviews', ascending = False).head())
      
      st.header('Halaman dengan jumlah pembaca halaman per sesi tertinggi')
      st.table(df_facebook.groupby(by='ga:pageTitle').agg({
          'ga:pageviewsPerSession': 'sum'
      }).sort_values(by='ga:pageviewsPerSession', ascending = False).head())
      
      st.header('Halaman dengan rata-rata waktu membaca halaman tertinggi')
      st.table(df_facebook.groupby(by='ga:pageTitle').agg({
          'ga:avgTimeOnPage': 'sum'
      }).sort_values(by='ga:avgTimeOnPage', ascending = False).head())

with tab2:
      st.header('Halaman dengan jumlah pengguna tertinggi')
      st.table(data=df_google.groupby(by='ga:pageTitle').agg({
            'ga:users': 'sum'
        }).sort_values(by='ga:users', ascending = False).head())
      
      st.header('Halaman dengan jumlah bounce rate tertinggi')
      st.table(df_google.groupby(by='ga:pageTitle').agg({
          'ga:pageviews': 'sum'
      }).sort_values(by='ga:pageviews', ascending = False).head())
      
      st.header('Halaman dengan jumlah pembaca halaman tertinggi')
      st.table(df_google.groupby(by='ga:pageTitle').agg({
          'ga:pageviews': 'sum'
      }).sort_values(by='ga:pageviews', ascending = False).head())
      
      st.header('Halaman dengan jumlah pembaca halaman per sesi tertinggi')
      st.table(df_google.groupby(by='ga:pageTitle').agg({
          'ga:pageviewsPerSession': 'sum'
      }).sort_values(by='ga:pageviewsPerSession', ascending = False).head())
      
      st.header('Halaman dengan rata-rata waktu membaca halaman tertinggi')
      st.table(df_google.groupby(by='ga:pageTitle').agg({
          'ga:avgTimeOnPage': 'sum'
      }).sort_values(by='ga:avgTimeOnPage', ascending = False).head())

st.image('heatmap.png')
      
