# Tugas 2 PBP

Pengenalan Aplikasi Django dan Models View Template (MVT) pada Django

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

Nama    : Qistina Muharrifa
NPM     : 2106708210

## Link Hasil Deploy
Hasil deploy bisa diakses melalui https://katalog-gg-geming.herokuapp.com/katalog/ 

## Bagan 

![Bagan]('../../staticfiles/bagan.png?raw=true')

Penjelasan :

Bagan yang berisi request client ke web aplikasi berbasis Django tersebut diawali dengan User yang melakukan request yang akan masuk ke framework `Django`. Setelah itu Django akan meneruskan ke `urls` untuk diproses dalam melakukan pencarian dan kemudian diteruskan ke `views` untuk diterima fungsinya. Fungsi yang ada pada views tersebut kana dijalankan dan menn-query data yang ada dengan `model` (yang melibatkan database) lalu terdapat proses transaksi data pada template. Proses request telah selesai, maka produk akan dikembalikan kembali sebagai bentuk response dan akan dirender pada template (HTML).

## Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Virtual environment (venv) digunakan untuk memastikan perubahan yang terjadi hanya pada venv saja dan tidak berubah pada local-storage. Hal ini digunakan untuk menjaga agar virtual tidak bertabrakan dengan versi lain. Lalu, membuat aplikasi web berbasis Django tanpa venv akan membuat update package program dan perubahaannya terjadi secara otomatis sehingga dapat mengubah data pada local-storage kita.

## Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.

1. views.py
   Diimplementasikan dengan membuat fungsi show_katalog dengan mengambil semua data yang ada pada database. Adapun saya menambahkan nama dan npm saya yang nantinya akan disimpan ke dalam variabel context dan kemudian akan di-render pada hasil return function show_katalog agar dapat munbul pada halaman HTML.

2. urls.py
   Diimplementasikan dengan penambbahan `path('katalog/', include('katalog.urls'))` pada urls_pattern yang berada pada project_django melakukan routing pada function show_katalo tadi agar dapat terlihat pada browser.

3. katalog.html
   Saya menambahkan variabel nama dan npm saya serta melakukan looping pada list_barang agar data-data yang ada pada database masuk ke tabel.

4. deployment
   Diimplementasikan dengan menghubungkan akun Github saya dengan Heroku dan tak lupa untuk melakukan deploy. Adapun penambahan variabel yang dibutuhkan (API keys serta nama app saya) yang akan dimasukan ke dalam serets variabel.


Sekian penjelasan saya, Terima kasih

Salam,
Qistina