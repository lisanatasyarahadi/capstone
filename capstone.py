from operator import index
import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt
import numpy as np

st.set_page_config(layout="wide")

df = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vQRU6kwdeypDfrGOupoOpxYxredNvgyib2zi6JZMAHY1mEaA1_dzw3cHA3btPT3W99QBjMmkoErvYKm/pub?gid=0&single=true&output=csv")
gdp = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vQRU6kwdeypDfrGOupoOpxYxredNvgyib2zi6JZMAHY1mEaA1_dzw3cHA3btPT3W99QBjMmkoErvYKm/pub?gid=541891748&single=true&output=csv")
rank = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vQRU6kwdeypDfrGOupoOpxYxredNvgyib2zi6JZMAHY1mEaA1_dzw3cHA3btPT3W99QBjMmkoErvYKm/pub?gid=1769985896&single=true&output=csv")

st.title("PISA SEBAGAI INDIKATOR CAPAIAN PENDIDIKAN")
st.image("PISA news post.png")
st.write("Nilai PISA menjadi topik hangat dalam dunia pendidikan dewasa ini. Terutama karena PISA 2021; yang seharusnya dilaksanakan tahun lalu dan tertunda karena pandemi; baru saja dilaksanakan pada tahun ini. Berkaca pada perolehan periode sebelumnya, bagaimanakah capaian Indonesia pada tahun ini? Sembari menantikan hasil yang nantinya akan dirilis oleh OECD ada baiknya kita melihat terlebih dahulu apa sebenarnya Tes PISA dan bagaimana hasil dari periode sebelumnya.")

st.header("Apa itu PISA Test?")
st.write("PISA adalah survei yang dilakukan setiap 3 tahun sekali terhadap siswa berusia 15 tahun di seluruh dunia. Tes PISA dilakukan untuk menilai sejauh mana siswa telah menguasai pengetahuan dan keterampilan yang dibutuhkan dalam kehidupan sosial dan ekonomi. Penilaian PISA tidak hanya memastikan apakah siswa menjelang akhir wajib belajar mereka dapat menggunakan ilmu yang telah mereka pelajari; PISA juga memeriksa seberapa baik siswa dapat menerapkan pengetahuan dan keterampilan yang telah mereka pelajari dalam berbagai konteks, baik di dalam maupun di luar sekolah.")
st.subheader("APA YANG UNIK TENTANG PISA?")
st.write("PISA unik karena:")
st.write("• orientasi kebijakan, yang menghubungkan data hasil belajar siswa dengan data tentang latar belakang dan sikap siswa terhadap pembelajaran, dan dengan faktor-faktor kunci yang membentuk pembelajaran mereka, di dalam dan di luar sekolah; dengan demikian, PISA dapat menyoroti perbedaan dalam kinerja dan mengidentifikasi karakteristik siswa, sekolah dan sistem pendidikan yang berkinerja baik")
st.write("• konsep inovatif “keaksaraan”, yang mengacu pada kapasitas siswa untuk menerapkan pengetahuan dan keterampilan mereka di bidang-bidang utama, dan untuk menganalisis, menalar, dan berkomunikasi secara efektif saat mereka mengidentifikasi, menafsirkan, dan memecahkan masalah dalam berbagai situasi")
st.write("• relevansi dengan pembelajaran sepanjang hayat, karena PISA meminta siswa untuk melaporkan motivasi mereka untuk belajar, keyakinan mereka tentang diri mereka sendiri, dan strategi belajar mereka • keteraturan, yang memungkinkan negara untuk memantau kemajuan mereka dalam memenuhi tujuan pembelajaran utama")
st.write("• cakupan yang luas, yang, dalam PISA 2018, mencakup 37 negara OECD dan 42 negara mitra dan ekonomi.")

st.subheader("Nilai PISA 2018")
st.write("Menjadi salah satu tolak ukur untuk menilai seberapa baik kualitas pendidikan di suatu negara tentunya membuat nilai PISA menjadi salah satu perhatian di dunia pendidikan. Nilai PISA yang dirilis terakhir adalah nilai PISA 2018. Mari kita lihat bagaimana capaian pada PISA 2018")

pilih = st.sidebar.selectbox("Pilih Nilai", ["Mean Reading", "Mean Math", "Mean Science"])


col1, col2 = st.columns(2)

with col1:
    st.write("""#Nilai PISA 2018 Berdasarkan Ranking""")
    pisa_sorted = df.sort_values(pilih)
    top_ten = pisa_sorted.loc[10:1]
    fig, ax = plt.subplots(figsize=(2.5,2.7))
    ax.barh(top_ten["Country Name"], top_ten[pilih], color="navy", height = 0.6)
    ax.set_title("Nilai PISA 10 Teratas")
    ax.set_xlabel(pilih)
    ax.set_ylabel("Nama Negara")
    st.pyplot(fig)

with col2:
    st.write("""#Nilai PISA dan GDP per Kapita""")
    fig2, ax = plt.subplots(figsize=(4,3.5))
    ax.scatter(gdp[pilih], gdp["GDP 2018"], color="royalblue")
    ax.set_xlabel(pilih)
    ax.set_ylabel("GDP per Kapita")
    st.pyplot(fig2)

st.write("Memperhatikan hasil dari PISA 2018, terlihat bahwa untuk semua mata pelajaran yang diujikan, posisi teratas diduduki oleh negara Asia seperti Singapura, China, dan juga Jepang. Posisi selanjutnya kemudian diikuti negara bagian Amerika dan juga Eropa.")
st.write("Selain daripada capaian nilai secara ranking, nilai PISA juga terkait dengan kondisi ekonomi suatu negara. Oleh karena OECD sendiri mengukur kemampuan siswa untuk hidup di masyarakat secara sosial ekonomi, kaitan perolehan nilai PISA dan kondisi ekonomi menjadi hal yang menarik untuk dipelajari lebih lanjut. Berdasarkan scatter plot terlihat bahwa ada hubungan antara nilai PISA dan juga GDP per kapita. Jika memperhatikan negara-negara yang menempati posisi teratas, sebagian besar didominasi oleh negara maju dengan perekonomian yang baik.")

st.subheader("Perolehan Nilai PISA 2012-2018")
st.write("Di bawan ini disajikan data nilai PISA selama 3 periode terakhir. Oleh karena PISA diadakan setiap 3 tahun sekali. Berikut adalah perolehan nilai PISA 2012, 2015, dan 2018.")

pilih_negara = st.selectbox("Pilih Negara", rank["Country Name"])
st.write("#Perolehan Nilai PISA 2012-2018", pilih_negara)

tab1, tab2, tab3 = st.tabs(["Nilai Mean Reading", "Nilai Mean Math", "Nilai Mean Science"])

with tab1:
    st.write("#Perolehan Nilai PISA 2012-2018")
    #pilih_negara = st.selectbox("Pilih Negara", rank["Country Name"])
    pisa_reading = pd.DataFrame(rank, columns=["Country Name", "Mean Reading 2012", "Mean Reading 2015", "Mean Reading 2018"])
    #st.dataframe(pisa_reading.set_index("Country Name"))
    pilih_negara_2 = pisa_reading.loc[pisa_reading["Country Name"] == pilih_negara]
    pilih_negara_3 = pilih_negara_2.set_index("Country Name")
    #st.dataframe(pilih_negara_a)
    pilih_negara_4 = pilih_negara_3.transpose()
    #st.dataframe(pilih_negara_3)
    st.bar_chart(pilih_negara_4)

with tab2:
    st.write("#Perolehan Nilai PISA 2012-2018")
    #pilih_negara_tab2 = st.selectbox("Pilih Negara", rank["Country Name"])
    pisa_math = pd.DataFrame(rank, columns=["Country Name", "Mean Math 2012", "Mean Math 2015", "Mean Math 2018"])
    pilih_negara_a = pisa_math.loc[pisa_math["Country Name"] == pilih_negara]
    pilih_negara_b = pilih_negara_a.set_index("Country Name")
    pilih_negara_c = pilih_negara_b.transpose()
    st.bar_chart(pilih_negara_c)
    
with tab3:
    st.write("#Perolehan Nilai PISA 2012-2018")
    #pilih_negara_tab3 = st.selectbox("Pilih Negara", rank["Country Name"])
    pisa_science = pd.DataFrame(rank, columns=["Country Name", "Mean Science 2012", "Mean Science 2015", "Mean Science 2018"])
    pilih_negara_d = pisa_science.loc[pisa_science["Country Name"] == pilih_negara]
    pilih_negara_e = pilih_negara_d.set_index("Country Name")
    pilih_negara_f = pilih_negara_e.transpose()
    st.bar_chart(pilih_negara_f)

st.subheader("Capaian PISA Indonesia")
asean = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vQRU6kwdeypDfrGOupoOpxYxredNvgyib2zi6JZMAHY1mEaA1_dzw3cHA3btPT3W99QBjMmkoErvYKm/pub?gid=186489749&single=true&output=csv")
OECD = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vQRU6kwdeypDfrGOupoOpxYxredNvgyib2zi6JZMAHY1mEaA1_dzw3cHA3btPT3W99QBjMmkoErvYKm/pub?gid=1583958311&single=true&output=csv")

st.write("Berikut adalah nilai capaian PISA Indonesia dibandingkan dengan rata-rata OECD dan juga negara tetangga")
col9, col10, col11 = st.columns(3)

with col9:
    st.write("#Nilai PISA: Reading")
    OECD_sorted = pd.DataFrame(OECD, columns=["Country Name", "Mean Reading 2012", "Mean Reading 2015", "Mean Reading 2018"])
    OECD_trans = OECD_sorted.set_index("Country Name")
    st.line_chart(OECD_trans.transpose())

with col10:
    st.write("#Nilai PISA Math")
    OECD_sorted = pd.DataFrame(OECD, columns=["Country Name", "Mean Math 2012", "Mean Math 2015", "Mean Math 2018"])
    OECD_trans = OECD_sorted.set_index("Country Name")
    st.line_chart(OECD_trans.transpose())
    
with col11:
    st.write("#Nilai PISA Science")
    OECD_sorted = pd.DataFrame(OECD, columns=["Country Name", "Mean Science 2012", "Mean Science 2015", "Mean Science 2018"])
    OECD_trans = OECD_sorted.set_index("Country Name")
    st.line_chart(OECD_trans.transpose())

st.write("Indonesia pada tahun 2018 sendiri mendapatkan peringkat 72 dari 79 untuk Reading, 72 dari 79 untuk Math, dan 71 dari 79 untuk Science. Pencapaian ini dapat dikatakan belum cukup baik. Mengingat nilai PISA menunjukkan kualitas pendidikan suatu negara maka nilai PISA Indonesia memperlihatkan kualitas pendidikan yang masih rendah.")
st.write("Pencapaian Indonesia selama 3 periode juga masih berada jauh di bawah rata-rata OECD dan menunjukkan capaian yang rendah untuk ketiga bidang. Dari hasil yang didapatkan selama 3 periode tidak ada perubahan signifikan bahkan cenderung menurun untuk keterampilan membaca (reading)")

tab4, tab5, tab6 =st.tabs(["Nilai Reading", "Nilai Math", "Nilai Science"])

with tab4:
    col3, col4 = st.columns(2)
    with col3:
        #use fivethirty eights style of plots
        plt.style.use("fivethirtyeight")
        #create the base axis to add the bars to
        fig3, ax = plt.subplots(1,1)
        #extract the labels
        label = asean["Country Name"]
        #use this to create x ticks to add the data to
        x = np.arange(len(label))
        #set a width for each bar 
        width = 0.2
        #create out first bar
        #set it so that x will be the centre of the bars
        #so that we can add our labels later
        #so set the centre of the first to be 1/2 width away
        #to the left
        rect1 = ax.bar(x - width/2,
                       asean["Mean Reading 2012"],
                       width = width,
                       label = "2012",
                       edgecolor = "black")
        #create the second bar
        #with a centre half a width to the right
        rect2 = ax.bar(x + width/2,
                       asean["Mean Reading 2015"],
                       width = width,
                       label = "2015",
                       edgecolor = "black")
        #create the third bar
        #with a centre a width to the right
        rect3 = ax.bar(x + width*3/2,
                       asean["Mean Reading 2018"],
                       width = width,
                       label = "2018",
                       edgecolor = "black")
        #add the labels to the axis
        ax.set_ylabel("Rata-rata Nilai",
                      fontsize = 10,
                      labelpad = 20)
        ax.set_xlabel("Nama Negara",
                      fontsize = 10,
                      labelpad =20)
        ax.set_title("Nilai PISA ASEAN 2012-2018: Reading",
                     fontsize = 12,
                     pad = 20)
        #set the ticks
        ax.set_xticks(x)
        ax.set_xticklabels(label)
        #add the legend
        #using the labels of the bars
        ax.legend(title = "Year of Test",
                  fontsize = 10,
                  title_fontsize = 10)
        #adjust the tick paramaters
        ax.tick_params(axis = "x",
                       which = "both",
                       labelsize = 10,
                       labelrotation = 45)
        ax.tick_params(axis = "y",
                       which = "both",
                       labelsize = 10)

        st.pyplot(fig3)
        
    with col4:
        #use fivethirty eights style of plots
        plt.style.use("seaborn-pastel")
        #create the base axis to add the bars to
        fig6, ax = plt.subplots(1,1)
        #extract the labels
        label = asean["Country Name"]
        #use this to create x ticks to add the data to
        x = np.arange(len(label))
        #set a width for each bar 
        width = 0.2
        #create out first bar
        #set it so that x will be the centre of the bars
        #so that we can add our labels later
        #so set the centre of the first to be 1/2 width away
        #to the left
        rect1 = ax.bar(x - width/2,
                       asean["Posisi Reading 2012"],
                       width = width,
                       label = "2012",
                       edgecolor = "black")
        #create the second bar
        #with a centre half a width to the right
        rect2 = ax.bar(x + width/2,
                       asean["Posisi Reading 2015"],
                       width = width,
                       label = "2015",
                       edgecolor = "black")
        #create the third bar
        #with a centre a width to the right
        rect3 = ax.bar(x + width*3/2,
                       asean["Posisi Reading 2018"],
                       width = width,
                       label = "2018",
                       edgecolor = "black")
        #add the labels to the axis
        ax.set_ylabel("Posisi Ranking",
                      fontsize = 10,
                      labelpad = 20)
        ax.set_xlabel("Nama Negara",
                      fontsize = 10,
                      labelpad =20)
        ax.set_title("Ranking PISA ASEAN 2012-2018: Reading",
                     fontsize = 12,
                     pad = 20)
        #set the ticks
        ax.set_xticks(x)
        ax.set_xticklabels(label)
        #add the legend
        #using the labels of the bars
        ax.legend(title = "Year of Test",
                  fontsize = 10,
                  title_fontsize = 10)
        #adjust the tick paramaters
        ax.tick_params(axis = "x",
                       which = "both",
                       labelsize = 10,
                       labelrotation = 45)
        ax.tick_params(axis = "y",
                       which = "both",
                       labelsize = 10)
        st.pyplot(fig6)
        
with tab5:
    col5, col6 = st.columns(2)
    with col5:
        #use fivethirty eights style of plots
        plt.style.use("fivethirtyeight")
        #create the base axis to add the bars to
        fig4, ax = plt.subplots(1,1)
        #extract the labels
        label = asean["Country Name"]
        #use this to create x ticks to add the data to
        x = np.arange(len(label))
        #set a width for each bar 
        width = 0.2
        #create out first bar
        #set it so that x will be the centre of the bars
        #so that we can add our labels later
        #so set the centre of the first to be 1/2 width away
        #to the left
        rect1 = ax.bar(x - width/2,
                       asean["Mean Math 2012"],
                       width = width,
                       label = "2012",
                       edgecolor = "black")
        #create the second bar
        #with a centre half a width to the right
        rect2 = ax.bar(x + width/2,
                       asean["Mean Math 2015"],
                       width = width,
                       label = "2015",
                       edgecolor = "black")
        #create the third bar
        #with a centre a width to the right
        rect3 = ax.bar(x + width*3/2,
                       asean["Mean Math 2018"],
                       width = width,
                       label = "2018",
                       edgecolor = "black")
        #add the labels to the axis
        ax.set_ylabel("Rata-rata Nilai",
                      fontsize = 10,
                      labelpad = 20)
        ax.set_xlabel("Nama Negara",
                      fontsize = 10,
                      labelpad =20)
        ax.set_title("Nilai PISA ASEAN 2012-2018: Math",
                     fontsize = 12,
                     pad = 20)
        #set the ticks
        ax.set_xticks(x)
        ax.set_xticklabels(label)
        #add the legend
        #using the labels of the bars
        ax.legend(title = "Year of Test",
                  fontsize = 10,
                  title_fontsize = 10)
        #adjust the tick paramaters
        ax.tick_params(axis = "x",
                       which = "both",
                       labelsize = 10,
                       labelrotation = 45)
        ax.tick_params(axis = "y",
                       which = "both",
                       labelsize = 10)

        st.pyplot(fig4)
        
    with col6:
        #use fivethirty eights style of plots
        plt.style.use("seaborn-pastel")
        #create the base axis to add the bars to
        fig6, ax = plt.subplots(1,1)
        #extract the labels
        label = asean["Country Name"]
        #use this to create x ticks to add the data to
        x = np.arange(len(label))
        #set a width for each bar 
        width = 0.2
        #create out first bar
        #set it so that x will be the centre of the bars
        #so that we can add our labels later
        #so set the centre of the first to be 1/2 width away
        #to the left
        rect1 = ax.bar(x - width/2,
                       asean["Posisi Math 2012"],
                       width = width,
                       label = "2012",
                       edgecolor = "black")
        #create the second bar
        #with a centre half a width to the right
        rect2 = ax.bar(x + width/2,
                       asean["Posisi Math 2015"],
                       width = width,
                       label = "2015",
                       edgecolor = "black")
        #create the third bar
        #with a centre a width to the right
        rect3 = ax.bar(x + width*3/2,
                       asean["Posisi Math 2018"],
                       width = width,
                       label = "2018",
                       edgecolor = "black")
        #add the labels to the axis
        ax.set_ylabel("Posisi Ranking",
                      fontsize = 10,
                      labelpad = 20)
        ax.set_xlabel("Nama Negara",
                      fontsize = 10,
                      labelpad =20)
        ax.set_title("Ranking PISA ASEAN 2012-2018: Math",
                     fontsize = 12,
                     pad = 20)
        #set the ticks
        ax.set_xticks(x)
        ax.set_xticklabels(label)
        #add the legend
        #using the labels of the bars
        ax.legend(title = "Year of Test",
                  fontsize = 10,
                  title_fontsize = 10)
        #adjust the tick paramaters
        ax.tick_params(axis = "x",
                       which = "both",
                       labelsize = 10,
                       labelrotation = 45)
        ax.tick_params(axis = "y",
                       which = "both",
                       labelsize = 10)

        st.pyplot(fig6)
        
with tab6:
    col7, col8 = st.columns(2)
    with col7:
        #use fivethirty eights style of plots
        plt.style.use("fivethirtyeight")
        #create the base axis to add the bars to
        fig5, ax = plt.subplots(1,1)
        #extract the labels
        label = asean["Country Name"]
        #use this to create x ticks to add the data to
        x = np.arange(len(label))
        #set a width for each bar 
        width = 0.2
        #create out first bar
        #set it so that x will be the centre of the bars
        #so that we can add our labels later
        #so set the centre of the first to be 1/2 width away
        #to the left
        rect1 = ax.bar(x - width/2,
                    asean["Mean Science 2012"],
                    width = width, 
                    label = "2012",
                    edgecolor = "black"
                    )
        #create the second bar
        #with a centre half a width to the right
        rect2 = ax.bar(x + width/2,
                    asean["Mean Science 2015"],
                    width = width,
                    label = "2015",
                    edgecolor = "black")
        #create the third bar
        #with a centre a width to the right
        rect3 = ax.bar(x + width*3/2,
                    asean["Mean Science 2018"],
                    width = width,
                    label = "2018",
                    edgecolor = "black")
        #add the labels to the axis
        ax.set_ylabel("Rata-rata Nilai",
                    fontsize = 10,
                    labelpad = 20)
        ax.set_xlabel("Nama Negara",
                    fontsize = 10,
                    labelpad =20)
        ax.set_title("Nilai PISA ASEAN 2012-2018: Science",
                    fontsize = 12,
                    pad = 20)
        #set the ticks
        ax.set_xticks(x)
        ax.set_xticklabels(label)
        #add the legend
        #using the labels of the bars
        ax.legend(title = "Year of Test",
                fontsize = 10,
                title_fontsize = 10)
        #adjust the tick paramaters
        ax.tick_params(axis = "x",
                    which = "both",
                    labelsize = 10,
                    labelrotation = 45)
        ax.tick_params(axis = "y",
                    which = "both",
                    labelsize = 10)
        st.pyplot(fig5)
        
    with col8:
        #use fivethirty eights style of plots
        plt.style.use("seaborn-pastel")
        #create the base axis to add the bars to
        fig6, ax = plt.subplots(1,1)
        #extract the labels
        label = asean["Country Name"]
        #use this to create x ticks to add the data to
        x = np.arange(len(label))
        #set a width for each bar 
        width = 0.2
        #create out first bar
        #set it so that x will be the centre of the bars
        #so that we can add our labels later
        #so set the centre of the first to be 1/2 width away
        #to the left
        rect1 = ax.bar(x - width/2,
                       asean["Posisi Science 2012"],
                       width = width,
                       label = "2012",
                       edgecolor = "black")
        #create the second bar
        #with a centre half a width to the right
        rect2 = ax.bar(x + width/2,
                       asean["Posisi Science 2015"],
                       width = width,
                       label = "2015",
                       edgecolor = "black")
        #create the third bar
        #with a centre a width to the right
        rect3 = ax.bar(x + width*3/2,
                       asean["Posisi Science 2018"],
                       width = width,
                       label = "2018",
                       edgecolor = "black")
        #add the labels to the axis
        ax.set_ylabel("Posisi Ranking",
                      fontsize = 10,
                      labelpad = 20)
        ax.set_xlabel("Nama Negara",
                      fontsize = 10,
                      labelpad =20)
        ax.set_title("Ranking PISA ASEAN 2012-2018: Science",
                     fontsize = 12,
                     pad = 20)
        #set the ticks
        ax.set_xticks(x)
        ax.set_xticklabels(label)
        #add the legend
        #using the labels of the bars
        ax.legend(title = "Year of Test",
                  fontsize = 10,
                  title_fontsize = 10)
        #adjust the tick paramaters
        ax.tick_params(axis = "x",
                       which = "both",
                       labelsize = 10,
                       labelrotation = 45)
        ax.tick_params(axis = "y",
                       which = "both",
                       labelsize = 10)
        st.pyplot(fig6)

st.write("Dibandingkan dengan negara tetangga, capaian Indonesia juga belum cukup baik. Indonesia mendapatkan peringkat kedua terbawah untuk negara ASEAN yang mengikuti Test PISA pada ketiga bidang.")
st.write("Perolehan yang belum maksimal ini tentunya perlu disikapi dengan bijaksana. Pemerintah beserta seluruh Instansi Pendidikan perlu melakukan transformasi sistem pendidikan yang signifikan untuk bisa meningkatkan kualitas pendidikan dan tentunya meningkatkan kualitas peserta didik. Oleh karena PISA mengukur kemampuan siswa dalam kehidupan bermasyarakat, bercermin pada nilai yang didapatkan Indonesia tentu kita perlu untuk membuat pembelajaran di dalam kelas menjadi lebih realistis dan dapat diaplikasikan dalam konteks bermasyarakat. Kemampuan siswa dalam literasi dan numerasi juga perlu untuk diperhatikan.")
st.write("Dengan meningkatkan kualitas pendidikan diharapkan bahwa bidang lain juga boleh meningkat oleh karena kualitas SDM yang lebih baik. Pemerintah terlihat sudah melakukan upaya perubahan terhadap sistem pendidikan. Semoga usaha ini dapat berjalan secara konsisten dan memberikan hasil yang salah satunya bisa dilihat pada periode Tes PISA mendatang.")
st.caption("Data diambil dari https://www.oecd.org/pisa/")