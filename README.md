# Bike Sharing
Ini adalah tugas akhir/proyek akhir “Belajar Analisis Data Dengan Python” untuk membuat analisis dan membuat dashboard dari dataset bike sharing. Pada file ini saya lampirkan cara menganalisa data dimulai dari Data Wrangling, Exploratory Data Analysis, dan Data Visualization. Selain itu saya juga membuat dashboardnya menggunakan streamlit, dan Anda bisa mengeceknya dengan mengklik link di sidebar kanan atau di sini.
Untuk informasi lebih lanjut, seperti latar belakang kumpulan data ini, karakteristik kumpulan data, struktur file, dan lainnya.

## 1. File Struktur
```

├── dashboard
│   ├── dashboard.py
├── data
│   ├── Readme.txt
│   ├── bike_day.csv
|   └── bike_hour.csv
├── README.md
├── notebook.ipynb
└── requirements.txt
```

## 2. Alur Kerja Analisis
    a. Data Wrangling:
        Gathering data
        Assessing data
        Cleaning data
    b. Exploratory Data Analysis:
        Pertanyaan bisnis  untuk eksplorasi data
        Buat tahap eksplorasi data
    c. Data Visualization:
        Buat Visualisasi Data yang menjawab pertanyaan bisnis.
    d. Dashboard:
        Siapkan DataFrame yang akan digunakan (Streamlit),
        Membuat komponen filter pada dashboard,
        Lengkapi dashboard dengan berbagai visualisasi data.



## 3. Memuat `notebook.ipynb`
1. Buka Google Colab atau Jupyter Notebook 
2. Klik File> Open Notebook> pilih lokasi penyimpanan file nootebook, semisal Upload (jika menyimpanan di device Komputer)
3. Pilih file yg berformat `notebook.ipynb`> open
4. Loading File> FIle sudah bisa digunakan

## 4. Dashboard 
 
1. Pastikan Anda memiliki lingkungan Python yang sesuai dan pustaka-pustaka yang diperlukan. Anda dapat menginstal pustaka-pustaka tersebut dengan menjalankan perintah berikut:
```shell
pip install streamlit 
```
2. Install juga library lainnya seperti pandas, numpy, scipy, matplotlib, dan seaborn jika belum terinstal.
```shell
pip install -r requirements.txt
```
3. diharapkan tidak memindahkan data `.csv` karena merupaka sumber data dashboard. biarkan tetap di dalam folder dashboard
4. Buka VSCode, dan jalankan file dengan menklik pada terminal and mengetik 
```shell
streamlit run dashboard1.py
```
5. Atau bisa dengan kunjungi website ini https://submission-agipx8mst7h3vuzx8s9xxv.streamlit.app/