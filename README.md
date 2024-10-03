# Dashboard Analisis Bike Sharing

## Setup Environment - Anaconda
Untuk setup environment menggunakan Anaconda, ikuti langkah-langkah berikut:

```bash
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```
## Setup Environment - Shell/Terminal
Jika kalian tidak menggunakan Anaconda, dapat menggunakan terminal dengan langkah-langkah berikut:

```bash
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```
## Run steamlit app
Setelah setup environment selesai, jalankan aplikasi Streamlit dengan perintah berikut:

```bash
streamlit run dashboard.py
```
Pastikan sudah berada pada path direktori yang tepat.