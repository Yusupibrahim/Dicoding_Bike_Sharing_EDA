import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st 


dayBike_df = pd.read_csv("day.csv", delimiter=",")
datetime_columns = ["dteday"]
 
for column in datetime_columns:
    dayBike_df[column] = pd.to_datetime(dayBike_df[column])

dayBike_desc_df = dayBike_df.describe(include="all")

sortCnt_df = dayBike_df.sort_values(['cnt'],ascending=False).groupby("season").head()
sortCasual_df = dayBike_df.sort_values(['casual'],ascending=False).groupby("season").head()

dayBikeAggCnt_df = dayBike_df.groupby(by="season").agg({
    "instant": "nunique",
    "cnt": ["max", "min", "mean", "std"],
    "workingday" : "mean",
    "weathersit" : "mean",
    "temp" : "mean",
    "atemp" : "mean",
    "hum" : "mean",
    "windspeed" : "mean" 
})

dayBikeAggCasual_df = dayBike_df.groupby(by="season").agg({
    "instant": "nunique",
    "casual": ["max", "min", "mean", "std"],
    "workingday" : "mean",
    "weathersit" : "mean",
    "temp" : "mean",
    "atemp" : "mean",
    "hum" : "mean",
    "windspeed" : "mean" 
})

fig_cnt = plt.figure(figsize=(10, 5)) 
plt.plot(dayBikeAggCnt_df["cnt"], marker='o', linewidth=2) 
plt.title("Number of Biker per Season", loc="center", fontsize=20)
plt.xlabel("Season")
plt.ylabel("Count")
plt.legend(["Max", "Min", "Mean","Standard"])
plt.xticks(fontsize=10) 
plt.yticks(fontsize=10) 

fig_casual = plt.figure(figsize=(10, 5)) 
plt.plot(dayBikeAggCasual_df["casual"], marker='o', linewidth=2) 
plt.title("Number of Biker per Season", loc="center", fontsize=20)
plt.xlabel("Season")
plt.ylabel("Count")
plt.legend(["Max", "Min", "Mean","Standard"])
plt.xticks(fontsize=10) 
plt.yticks(fontsize=10) 


st.title('Analisis Data Pesepeda Cnt dan Casual')
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Deskripsi","Raw", "Sort","Aggregat", "Plot"])
 
with tab1:
    st.header("Deskripsi")
    st.write(dayBike_desc_df)
 
with tab2:
    st.header("Raw")
    st.write(dayBike_df)
 
with tab3:
    st.header("Sort")
    st.markdown("""---""")
    st.subheader("Table Sort Descending Max Cnt")
    st.write(sortCnt_df)
    st.subheader("Table Sort Descending Max Casual")
    st.write(sortCasual_df)
with tab4:
    st.header("Aggregat")
    st.markdown("""---""")
    st.subheader("Table Aggregat Cnt")
    st.write(dayBikeAggCnt_df)
    st.subheader("Table Aggregat Casual")
    st.write(dayBikeAggCasual_df)
with tab5:
    st.header("Plot")
    st.markdown("""---""")
    st.subheader("Trend Season Cnt")
    st.pyplot(fig_cnt)
    with st.expander("Kesimpulan Pertanyaan 1"):
        st.write(
        """Kesimpulan pertanyaan 1 didapat bawasannya agar total semua peseda terbanyak diperlukan faktor situasi cuaca yang bersih dan sedikit berawan, temperatur rata-rata 0.7 atau 29 derajat celcius, rasa temperatur rata-rata 0.65 atau 32 derajat celcius, kelembapan rata-rata 63, dan kecepatan udara 0.17 atau 11. selain itu, bisa dilihat juga bahwa rata-rata pesepeda dapat meluangkan waktu pada hari kerjanya. dengan faktor diatas didapat musim dengan jumlah peserta pesepeda paling banyak yaitu musim gugur.
        """
    )
    st.subheader("Trend Season Casual")
    st.pyplot(fig_casual)
    with st.expander("Kesimpulan Pertanyaan 2"):
        st.write(
        """Kesimpulan pertanyaan 2 didapat bawasannya agar total semua peseda casual terbanyak diperlukan faktor situasi cuaca yang bersih dan sedikit berawan, temperatur rata-rata 0.5 atau 20 derajat celcius, rasa temperatur rata-rata 0.5 atau 25 derajat celcius, kelembapan rata-rata 63, dan kecepatan udara 0.2 atau 13. selain itu, bisa dilihat juga bahwa rata-rata pesepeda dapat meluangkan waktu pada hari kerjanya. dengan faktor diatas didapat musim dengan jumlah peserta pesepeda casual paling banyak yaitu musim panas.
        """
    )
 
