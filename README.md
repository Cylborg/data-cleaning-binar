# data-cleaning-binar
Data Science Challenge API Cleansing

Kode yang diberikan adalah sebuah skrip Python yang membuat dua endpoint untuk sebuah aplikasi web Flask.

Endpoint pertama, yang berada di '/api/clean_file', menerima unggahan file dengan format CSV dan melakukan pembersihan data dengan menghapus karakter non-alphanumerik, menghapus kata pendek dan panjang, menghapus spasi berlebih, menormalisasi teks, dan menghapus kata kasar. Data yang telah dibersihkan kemudian disimpan ke file CSV dan database SQLite.

Endpoint kedua, yang berada di '/api/clean_text', menerima masukan teks dan melakukan pembersihan data yang sama dengan menghapus RT, nama pengguna, URL, tanda baca, digit, dan kata-kata kasar. Teks yang telah dibersihkan kemudian dikembalikan sebagai respons dari endpoint.

Kode ini juga mencakup konfigurasi untuk dokumentasi Swagger UI dan mengimpor pustaka-pustaka yang diperlukan seperti Flask, pandas, dan re.
