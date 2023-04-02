# **data-cleaning-binar**
##**Data Science Challenge API Cleansing**

Kode yang diberikan adalah sebuah skrip Python dengan judul app.py yang membuat dua endpoint untuk sebuah aplikasi web Flask.

Endpoint pertama, yang berada di '/api/clean_file', menerima unggahan file dengan format CSV dan melakukan pembersihan data dengan menghapus karakter non-alphanumerik, menghapus kata pendek dan panjang, menghapus spasi berlebih, menormalisasi teks, dan menghapus kata kasar. Data yang telah dibersihkan kemudian disimpan ke file CSV dan database SQLite.

Endpoint kedua, yang berada di '/api/clean_text', menerima masukan teks dan melakukan pembersihan data yang sama dengan menghapus RT, nama pengguna, URL, tanda baca, digit, dan kata-kata kasar. Teks yang telah dibersihkan kemudian dikembalikan sebagai respons dari endpoint.

Ada juga skrip python EDA.PY yang berfungsi untuk memberikan visualisasi pada data "cleaned_data.csv" yang dihasilkan oleh "app.py.

Kode ini juga mencakup konfigurasi untuk dokumentasi Swagger UI dan mengimpor pustaka-pustaka yang diperlukan seperti Flask, pandas, dan re, matplotlib, seaborn dan wordcloud.

# **Petunjuk Penggunaan API**
## **Instalasi**
1. Clone repository ini.

```
git clone https://github.com/Cylborg/data-cleaning-binar
```

2. Install dependensi yang dibutuhkan

```
pip install pandas matplotlib flask flask_swagger_ui
```

3. Jalankan API app.py

```
python app.py
```

## **Penggunaan**

1. Setelah API berjalan, buka browser dan buka

```
http://127.0.0.1:5000/api/docs/#/default/post_api_clean_file
```

2. Untuk membersihkan file
    * Endpoint ini digunakan untuk membersihkan file CSV
    * pilih clean file 
    * pilih Input file CSV yang akan dibersihkan.
    * outputnya berupa file csv "cleaned_data.csv"
    
3. Untuk membersihkan text
   * Endpoint ini digunakan untuk membersihkan teks.
   * pilih clean text
   * Input text: teks yang akan dibersihkan.
   * Text yang telah dibersihkan akan muncul
   
4. Untuk mendapatkan visualisasi dari data yang telah dibersihkan, jalankan EDA.py

```
python eda.py
```



## **Tentang Dataset** 
Penulis asli GitHub: https://github.com/okkyibrohim/id-multi-label-hate-speech-and-abusive-language-detection
Saya mengunggahnya ke github karena saya menggunakannya untuk tugas Gold Challenge dari Binar saya di sini. Semua kredit diberikan kepada penulis asli.


##**Kutipan**

Muhammad Okky Ibrohim dan Indra Budi. 2019. Deteksi Bahasa Kasar dan Ujaran Kebencian Multi-label pada Twitter Indonesia. Dalam ALW3: 3rd Workshop on Abusive Language Online, 46-57. 
