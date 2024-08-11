import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.title('Analisis Kinerja Halaman Web Berdasarkan Sumber Lalu Lintas')
st.markdown('- Python libraries: numpy, pandas, streamlit, matplotlib, seaborn')
st.markdown('- Data source: https://docs.google.com/spreadsheets/d/1HoTUoAWX3jdS3WPz6chBwiEzj7BHD4uSd5Flx3bsbWE/edit?usp=sharing')

df = pd.read_csv('new_data.csv')
df_facebook = df[df['ga:sourceMedium'] == 'facebook / cpc']
df_google = df[df['ga:sourceMedium'] == 'google / cpc']

st.header('Statistika deskriptif')
st.table(df.describe().T)

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
st.markdown('- Grafik heatmap ini menunjukkan bahwa jumlah pengguna, tampilan halaman, tampilan halaman per sesi, dan rata-rata waktu per halaman saling berhubungan erat, yang berarti meningkatkan satu metrik kemungkinan besar akan meningkatkan yang lain.')
st.markdown('- Sebaliknya, bounce rate lebih sulit diprediksi berdasarkan metrik-metrik lainnya dan mungkin memerlukan analisis lebih lanjut atau strategi khusus untuk pengelola situs web yang ingin menurunkannya.')

st.header('Rata-rata users facebook dan google')
st.image('download.png')
st.write('Facebook memiliki rata-rata jumlah pengguna yang jauh lebih tinggi dibandingkan dengan Google. Rata-rata pengguna dari Facebook adalah 3575, sedangkan dari Google hanya 159.')

st.header('Rata-rata bounce rate facebook dan google')
st.image('download (1).png')
st.write('Google memiliki rata-rata bounce rate yang sedikit lebih tinggi dibandingkan dengan Facebook. Rata-rata bounce rate dari Facebook adalah 58, sedangkan dari Google hanya 57.')

st.header('Rata-rata page views facebook dan google')
st.image('download (2).png')
st.write('Facebook memiliki rata-rata jumlah pembaca halaman yang jauh lebih tinggi dibandingkan dengan Google. Rata-rata jumlah pembaca halaman dari Facebook adalah 6273, sedangkan dari Google hanya 290.')

st.header('Rata-rata page views per session facebook dan google')
st.image('download (3).png')
st.write('Facebook memiliki rata-rata jumlah pembaca halaman per sesi yang sedikit lebih tinggi dibandingkan dengan Google. rata-rata jumlah pembaca halaman per sesi dari Facebook adalah 18, sedangkan dari Google hanya 12.')

st.header('Rata-rata average time on page facebook dan google')
st.image('download (4).png')
st.write('Facebook memiliki rata-rata waktu membaca halaman yang lebih tinggi dibandingkan dengan Google. rata-rata waktu membaca halaman dari Facebook adalah 104, sedangkan dari Google hanya 79.')

st.header('Evaluasi')
st.markdown('- Metrik bounce rate menunjukkan korelasi yang rendah dengan metrik lainnya dalam heatmap ini. Hal ini berarti bounce rate mungkin tidak dapat diprediksi atau dikendalikan hanya dengan meningkatkan metrik lain seperti jumlah pengguna atau tampilan halaman. Bounce rate mungkin memerlukan analisis lebih mendalam atau pendekatan yang berbeda untuk pengelola situs web jika mereka ingin menurunkan angka ini.')
st.markdown('- Facebook secara signifikan unggul dibandingkan dengan Google dalam hal jumlah pengguna, keterlibatan, dan interaksi pada halaman. Rata-rata jumlah pengguna Facebook jauh lebih tinggi, mencapai 3575 dibandingkan dengan Google yang hanya 159. Selain itu, Facebook juga mencatat rata-rata jumlah pembaca halaman yang lebih tinggi, yaitu 6273, dibandingkan dengan 290 dari Google. Meskipun selisihnya tidak terlalu besar, Facebook juga mengungguli Google dalam metrik rata-rata jumlah pembaca halaman per sesi (18 dibandingkan dengan 12) dan rata-rata waktu membaca halaman (104 detik dibandingkan dengan 79 detik). Namun, dalam hal bounce rate, kedua platform menunjukkan hasil yang hampir sama, dengan Google memiliki rata-rata bounce rate yang sedikit lebih tinggi (57) dibandingkan dengan Facebook (58).')
st.write('Secara keseluruhan, data ini menunjukkan bahwa pengguna Facebook tidak hanya lebih banyak, tetapi juga lebih terlibat dengan konten, menghabiskan lebih banyak waktu di halaman, dan menjelajahi lebih banyak konten per sesi dibandingkan dengan pengguna Google. Bagi pemasar atau pengelola situs, hal ini menunjukkan potensi yang lebih besar untuk mendapatkan interaksi yang lebih dalam dan berarti dari pengguna yang datang melalui Facebook dibandingkan dengan Google.')
            
      
