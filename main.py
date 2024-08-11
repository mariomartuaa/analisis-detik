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

st.header('Korelasi antar field')
st.image('heatmap.png')

st.header('Rata-rata users facebook dan google')
st.image('download.png')

st.header('Rata-rata bounce rate facebook dan google')
st.image('download (1).png')

st.header('Rata-rata page views facebook dan google')
st.image('download (2).png')

st.header('Rata-rata page views per session facebook dan google')
st.image('download (3).png')

st.header('Rata-rata average time on page facebook dan google')
st.image('download (4).png')'

st.header('Evaluasi')
st.markdown('-Metrik bounce rate menunjukkan korelasi yang rendah dengan metrik lainnya dalam heatmap ini. Hal ini berarti bounce rate mungkin tidak dapat diprediksi atau dikendalikan hanya dengan meningkatkan metrik lain seperti jumlah pengguna atau tampilan halaman. Bounce rate mungkin memerlukan analisis lebih mendalam atau pendekatan yang berbeda untuk pengelola situs web jika mereka ingin menurunkan angka ini.')
st.markdown('- Facebook secara signifikan unggul dibandingkan dengan Google dalam hal jumlah pengguna, keterlibatan, dan interaksi pada halaman. Rata-rata jumlah pengguna Facebook jauh lebih tinggi, mencapai 3575 dibandingkan dengan Google yang hanya 159. Selain itu, Facebook juga mencatat rata-rata jumlah pembaca halaman yang lebih tinggi, yaitu 6273, dibandingkan dengan 290 dari Google. Meskipun selisihnya tidak terlalu besar, Facebook juga mengungguli Google dalam metrik rata-rata jumlah pembaca halaman per sesi (18 dibandingkan dengan 12) dan rata-rata waktu membaca halaman (104 detik dibandingkan dengan 79 detik). Namun, dalam hal bounce rate, kedua platform menunjukkan hasil yang hampir sama, dengan Google memiliki rata-rata bounce rate yang sedikit lebih tinggi (57) dibandingkan dengan Facebook (58).')
st.write('Secara keseluruhan, data ini menunjukkan bahwa pengguna Facebook tidak hanya lebih banyak, tetapi juga lebih terlibat dengan konten, menghabiskan lebih banyak waktu di halaman, dan menjelajahi lebih banyak konten per sesi dibandingkan dengan pengguna Google. Bagi pemasar atau pengelola situs, hal ini menunjukkan potensi yang lebih besar untuk mendapatkan interaksi yang lebih dalam dan berarti dari pengguna yang datang melalui Facebook dibandingkan dengan Google.')
            
      
