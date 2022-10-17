from cProfile import label
from ctypes.wintypes import SIZE
from email.policy import default
from turtle import color, title
import tkinter as TK
import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt
#import numpy as np
#import seaborn as sns
#import plotly.express as px

st.set_page_config(layout="wide")

df = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vQRU6kwdeypDfrGOupoOpxYxredNvgyib2zi6JZMAHY1mEaA1_dzw3cHA3btPT3W99QBjMmkoErvYKm/pub?gid=0&single=true&output=csv")
gdp = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vQRU6kwdeypDfrGOupoOpxYxredNvgyib2zi6JZMAHY1mEaA1_dzw3cHA3btPT3W99QBjMmkoErvYKm/pub?gid=541891748&single=true&output=csv")
#gdp_2 = pd.read_csv("PISA GDP 2018 - Copy.csv")

st.title("PISA SEBAGAI INDIKATOR CAPAIAN PENDIDIKAN")
st.write("Nilai PISA menjadi topik hangat dalam dunia pendidikan dewasa ini. Terutama karena PISA 2021 yang seharusnya dilaksanakan tahun lalu dan tertunda karena pandemi baru saja dilaksanakan pada tahun ini. Berkaca pada perolehan periode sebelumnya, bagaimanakah capaian Indonesia pada tahun ini? Sembari menantikan hasil yang nantinya akan dirilis oleh OECD ada baiknya kita melihat terlebih dahulu apa sebenarnya Tes PISA dan bagaimana hasil dari periode sebelumnya.")

st.header("Apa itu PISA Test?")
st.write("PISA adalah survei yang dilakukan setiap 3 tahun sekali terhadap siswa berusia 15 tahun di seluruh dunia. Tes PISA dilakukan untuk menilai sejauh mana siswa telah menguasai pengetahuan dan keterampilan yang dibutuhkan dalam kehidupan sosial dan ekonomi. Penilaian PISA tidak hanya memastikan apakah siswa menjelang akhir wajib belajar mereka dapat menggunakan ilmu yang telah mereka pelajari; PISA juga memeriksa seberapa baik siswa dapat menerapkan pengetahuan dan keterampilan yang telah mereka pelajari dalam berbagai konteks, baik di dalam maupun di luar sekolah.")
st.subheader("APA YANG UNIK TENTANG PISA?")
st.write("PISA unik karena: • orientasi kebijakan, yang menghubungkan data hasil belajar siswa dengan data tentang latar belakang dan sikap siswa terhadap pembelajaran, dan dengan faktor-faktor kunci yang membentuk pembelajaran mereka, di dalam dan di luar sekolah; dengan demikian, PISA dapat menyoroti perbedaan dalam kinerja dan mengidentifikasi karakteristik siswa, sekolah dan sistem pendidikan yang berkinerja baik • konsep inovatif “keaksaraan”, yang mengacu pada kapasitas siswa untuk menerapkan pengetahuan dan keterampilan mereka di bidang-bidang utama, dan untuk menganalisis, menalar, dan berkomunikasi secara efektif saat mereka mengidentifikasi, menafsirkan, dan memecahkan masalah dalam berbagai situasi • relevansi dengan pembelajaran sepanjang hayat, karena PISA meminta siswa untuk melaporkan motivasi mereka untuk belajar, keyakinan mereka tentang diri mereka sendiri, dan strategi belajar mereka • keteraturan, yang memungkinkan negara untuk memantau kemajuan mereka dalam memenuhi tujuan pembelajaran utama • cakupan yang luas, yang, dalam PISA 2018, mencakup 37 negara OECD dan 42 negara mitra dan ekonomi.")

st.write("""#Tabel Nilai PISA""")
st.dataframe(df)
#st.dataframe(gdp)
#st.dataframe(gdp_2)

st.write("""#Nilai PISA dan GDP""")

#st.bar_chart(
    #data = gdp,
    #x = 'Country Name',
    #y = st.selectbox("Pilih Nilai", ["Mean Reading", "Mean Math", "Mean Science", "GDP 2018"]))

#plotdata = gdp.plot(kind="barh")
#plt.title("Nilai PISA dan GDP")
#plt.ylabel("Country Name")
#plt.xlabel("Mean Math")
#st.pyplot(plotdata)

pilih = st.selectbox("Pilih Nilai", ["Mean Reading", "Mean Math", "Mean Science"])

pisa_sorted = df.sort_values(pilih)
fig, ax = plt.subplots(figsize = (3, 12))
ax.barh(pisa_sorted["Country Name"], pisa_sorted[pilih], color="Blue", height = 0.5)
ax.set_title("Nilai PISA")
ax.set_xlabel(pilih)
ax.set_ylabel("Nama Negara")
st.pyplot(fig)

fig2, ax = plt.subplots()
ax.scatter(gdp[pilih], gdp["GDP 2018"])
st.pyplot(fig2)
#st.pyplot(plt.scatter(
    #data=gdp_2,
    #x='Country Name',
    #y='Mean Reading')
#)

st.caption("Data diambil dari https://www.oecd.org/pisa/")
