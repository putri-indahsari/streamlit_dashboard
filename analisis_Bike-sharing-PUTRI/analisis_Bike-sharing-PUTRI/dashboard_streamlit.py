import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Judul Dashboard
st.title("Dashboard Analisis Penyewaan Sepeda (2011-2012)")

# Deskripsi
st.write("""
Dashboard ini menampilkan analisis dan visualisasi data penyewaan sepeda berdasarkan musim, hari libur, dan suhu.
""")

# Load Data (gantikan dengan dataset Anda)
# Misalnya, day_df adalah DataFrame dengan kolom: 'season', 'holiday', 'temp', 'cnt'
# Contoh data:
data = {
    'season': [1, 2, 3, 4, 1, 2, 3, 4],  # 1: Winter, 2: Spring, 3: Summer, 4: Fall
    'holiday': [0, 0, 1, 0, 1, 0, 1, 0],  # 0: Hari Biasa, 1: Hari Libur
    'temp': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8],  # Suhu (normalisasi)
    'cnt': [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000]  # Jumlah Penyewaan
}
day_df = pd.DataFrame(data)

# Sidebar untuk Filter Data
st.sidebar.header("Filter Data")
selected_season = st.sidebar.selectbox("Pilih Musim", options=["All", "Winter", "Spring", "Summer", "Fall"])
selected_holiday = st.sidebar.selectbox("Pilih Hari Libur", options=["All", "Hari Biasa", "Hari Libur"])

# Filter Data berdasarkan Pilihan Pengguna
if selected_season != "All":
    season_map = {"Winter": 1, "Spring": 2, "Summer": 3, "Fall": 4}
    day_df = day_df[day_df['season'] == season_map[selected_season]]

if selected_holiday != "All":
    holiday_map = {"Hari Biasa": 0, "Hari Libur": 1}
    day_df = day_df[day_df['holiday'] == holiday_map[selected_holiday]]

# Tampilkan Data yang Difilter
st.write("### Data yang Difilter")
st.write(day_df)

# Visualisasi 1: Distribusi Penyewaan Sepeda per Musim
st.write("### Distribusi Penyewaan Sepeda per Musim")
plt.figure(figsize=(10, 6))
sns.barplot(x='season', y='cnt', data=day_df, ci=None, palette='viridis')
plt.title('Distribusi Penyewaan Sepeda per Musim')
plt.xlabel('Musim (1 = Winter, 2 = Spring, 3 = Summer, 4 = Fall)')
plt.ylabel('Jumlah Penyewaan Sepeda')
st.pyplot(plt)

# Visualisasi 2: Hubungan Suhu dan Penyewaan Sepeda
st.write("### Hubungan Suhu dan Penyewaan Sepeda")
plt.figure(figsize=(10, 6))
sns.scatterplot(x='temp', y='cnt', hue='holiday', data=day_df, palette={0: 'blue', 1: 'yellow'}, s=100)
plt.title('Hubungan Suhu dan Penyewaan Sepeda')
plt.xlabel('Suhu (Normalisasi)')
plt.ylabel('Jumlah Penyewaan Sepeda')
plt.legend(title='Hari Libur', labels=['Hari Biasa', 'Hari Libur'])
st.pyplot(plt)

# Visualisasi 3: Penyewaan Sepeda pada Hari Libur vs Hari Biasa
st.write("### Penyewaan Sepeda pada Hari Libur vs Hari Biasa")
plt.figure(figsize=(8, 5))
sns.boxplot(x='holiday', y='cnt', data=day_df, palette='pastel')
plt.title('Penyewaan Sepeda pada Hari Libur vs Hari Biasa')
plt.xlabel('Hari Libur (0 = Hari Biasa, 1 = Hari Libur)')
plt.ylabel('Jumlah Penyewaan Sepeda')
st.pyplot(plt)