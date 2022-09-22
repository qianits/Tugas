### Jelaskan perbedaan antara JSON, XML, dan HTML!

​​JSON atau JavaScript Object Notation adalah sebuah format yang digunakan untuk menyimpan, membaca, serta menukar informasi dari web server sehingga dapat terbaca oleh semua orang.  File .json berisi teks yang berisi dua elemen inti, yaitu key dan value:
Key	: Berisi urutan karakter yang diapit oleh tanda kutip
Value	: Merupakan tipe data JSON yang solid, yaitu bisa berbentuk array, objek, string, boolean, angka atau null.

XML atau Extensible Markup Language adalah konten yang akan menyimpan data dalam format teks yang sederhana. Berbeda dengan JSON, XML menyimpan elemen-elemennya dengan cara terstruktur, mudal dibaca oleh manusia dan mesin tetapi kurang efisien. XML ini mirip dengan HTML.

HTML atau HyperText Markup Language tersusun atas tag-tag yang mengatur bagaimana data dalam file itu akan ditampilkan, tetapi tidak ada informasi mengenai isi dari data tersebut. HTML ini berfokus terhadap penyajian data. 

### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Kita memerlukan data delivery dalam pengimplementasian sebuah platform karena kita membutuhkan proses pertukaran data, yaitu dari database dan mengirimkan template melalui views. Penggunaan metode data delivery di sini (JSON, XML, dan HTML) menjadi lebih mudah dan mempermudah para developer dikarenakan mudah dibaca oleh banyak orang.

### Penjelasan Checklist

- Membuat aplikasi dengan menjalankan command pada env, yaitu python manage.py startapp mywatchlist, sehingga muncul path baru yaitu mywatchlist
- Lalu, pada project_django/urls.py ditambahkan path('mywatchlist/', include('mywatchlist.urls')) untuk menghubungkan urlpatterns pada mywatchlist/urls.py dengan urlpatterns pada project_django/urls.py. Pada mywatchilst/urls.py ditambahkan pattern path-path yang diminta ke views yang sesuai, yaitu XML, HTML, dan JSON.
- Pada mywatchlist, kita membuat class (models) pada models.py yang nantinya berfungsi untuk menambahkan 10 objek/data yang diinginkan pada fixtures (.json) dengan nama MyWatchList. Setelah itu kita melakukan migrations.
- Melakukan routing dengan ….. agar dapat terlihat melalui URL HTML, XML, maupun JSON
- Melakukan deploy dengan melakukan push ke main.

### Postman

JSON


HTML



XML



