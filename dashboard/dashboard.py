# dashboard.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import altair as alt

# judul aplikasi
st.title("Dashboard Analisis Penyewaan Sepeda")

# Load data csv
df = pd.read_csv("dashboard/main_data.csv")

# Konversi 'season' dan 'workday'
season_labels = ['Spring', 'Summer', 'Fall', 'Winter']
df['season'] = df['season'].map({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})
df['workingday'] = df['workingday'].map({0: 'Hari Libur', 1: 'Hari Kerja'})

# Sidebar filter
st.sidebar.header("Filter Data")
season_filter = st.sidebar.multiselect('Filter berdasarkan Musim', season_labels, default=season_labels)
workday_filter = st.sidebar.multiselect('Filter berdasarkan Hari Kerja/Libur', ['Hari Kerja', 'Hari Libur'], default=['Hari Kerja', 'Hari Libur'])

# Filter data berdasarkan pilihan user
filtered_data = df[df['season'].isin(season_filter) & df['workingday'].isin(workday_filter)]


# Visualisasi perbandingan musim
st.text("")
st.subheader("Rata-rata Penyewaan Sepeda per Musim")
seasonal = filtered_data.groupby('season')['cnt'].mean()

fig, ax = plt.subplots()
sns.barplot(x=seasonal.index, y=seasonal.values, palette=['#9c5708', '#ce6a85', 'orange', '#c0f6fb'], ax=ax)
ax.set_title('Average Bike Rentals by Season')
ax.set_xlabel('Season')
ax.set_ylabel('Average Rentals')
st.pyplot(fig)


# Visualisasi perbandingan hari kerja dan libur
st.text("")
st.subheader("Penyewaan Sepeda Berdasarkan Hari Kerja vs Hari Libur")
workday_counts = filtered_data.groupby('workingday')['cnt'].mean()

fig, ax = plt.subplots()
sns.barplot(x=workday_counts.index, y=workday_counts.values, palette=['#b06500', '#222987'], ax=ax)
ax.set_title('Rata-rata Penyewaan Sepeda: Hari Kerja vs Hari Libur')
ax.set_xlabel('Kategori Hari')
ax.set_ylabel('Rata-rata Penyewaan')
st.pyplot(fig)


# Tambahan: Visualisasi total penyewaan sepeda berdasarkan musim dan kategori hari
st.text("")
st.subheader("Total Penyewaan Sepeda")
# Buat dataframe baru
data = pd.DataFrame({
    'season': ['Spring', 'Spring', 'Summer', 'Summer', 'Fall', 'Fall', 'Winter', 'Winter'],
    'workingday': [1, 0, 1, 0, 1, 0, 1, 0],  # 1 = Hari Kerja, 0 = Hari Libur
    'cnt': [250000, 100000, 450000, 200000, 700000, 300000, 500000, 200000]
})
data['workingday_label'] = data['workingday'].apply(lambda x: 'Hari Kerja' if x == 1 else 'Hari Libur')

# Buat grouped bar chart menggunakan Altair
chart = alt.Chart(data).mark_bar(size=35).encode(
    x=alt.X('workingday_label', title=''),
    y=alt.Y('cnt:Q', title='Jumlah Penyewaan Sepeda'),
    color=alt.Color('workingday_label', legend=alt.Legend(title="Tipe Hari")),
    column=alt.Column('season:N', title='')
).properties(
    width=150,
    height=400,
).configure_header(
    labelOrient='bottom'
).configure_facet(
    spacing=5
)
st.altair_chart(chart)



# Kluster berdasarkan jumlah usage/penyewaan
labels = ['Low Usage', 'Medium Usage', 'High Usage']
bins = [0, 3000, 6000, df['cnt'].max()]
df['usage_cluster'] = pd.cut(df['cnt'], bins=bins, labels=labels, include_lowest=True)

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='dteday', y='cnt', hue='usage_cluster', palette='Set1')
plt.title('Scatter Plot Penyewaan Sepeda Harian Berdasarkan Usage Cluster')
plt.xlabel('Waktu')
plt.ylabel('Jumlah Penyewaan Sepeda (cnt)')
plt.legend(title='Usage Cluster')

st.pyplot(plt)




footer_html = """<footer>
  <p>© 2024 Dashboard Analisis Penyewaan Sepeda</p>
</footer>"""
st.markdown(footer_html, unsafe_allow_html=True)
