# Tugas 6 PBP - Javascript dan AJAX

[Link Deployment](https://katalog-gg-geming.herokuapp.com/todolist/)

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming
Pada asynchronous programming, kita dapat memberikan input sebanyak apapun dan akan diproses bersamaan sehingga tidak perlu menunggu bari kode sebelumnya selesai. Metode ini menjadikan web lebih efisien karena beberapa task dapat dijalankan secara bersamaan.

Pasda synchronus programming, kita perlu menginput satu-satu dan metode ini perlu menunggu parameter atau perintah sebelumnya berjalan sehingga task harus dijalankan secara urut. Metode ini kurang efisien, karena contohnya pada tugas lab sebelumnya, kita perlu refresh ulang agar data selalu up-to-date.

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini
Event-driven programming merupakan paradigma dalam programming di mana aliran program ditentukan oleh peristiwa seperti tindakan pengguna (klik mouse, penekanan tombol), keluaran sensor, atau pesan dari program lain. Contoh penerapannya pada tugas ini adalah $("#create-btn").click(function() dimana button "create new task" akan diclick.

##  Jelaskan penerapan asynchronous programming pada AJAX
Jika ada sebuah event terjadi, event tersebut akan mengakibatkan sebuah fungsionalitas AJAX dijalankan. Contoh penerapan asynchronous pada AJAX adalah kita dapat event driven programming yang sudah disebutkan pada sebelumnya. AJAX akan menampung perintah yang akan dijalankan lalu mengirimkannya ke server agar datanya diubah secara asynchronous.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Untuk AJAX get, pada views.py ditambahkan sebuah function untuk mengembalikan Task yang sesuai dengan user logged in dalam bentuk JSON. Views tersebut dihubungkan dengan routing /todolist/json yang ditambahkan di urls.py. Ketika website selesai di-load, dilakukan pemanggilan AJAX GET untuk mendapatkan Task dalam bentuk JSON, kemudian dimasukkan ke dalam tabel. Selain itu, terdapat AJAX post. Penerapannya ialah tombol buat task yang sebelumnya melakukan redirect ke todolist/create_task diubah menjadi tidak melakukan redirect, tetapi memunculkan sebuah modal. Pada modal tersebut berisi sebuah form. Ketika form tersebut diisi dan button untuk tambah task diklik, akan dilakukan pemanggilan AJAX post. Data tersebut akan dikirim ke server dan jika berhasil membuat task baru, modal tersbeut akan ditutup kembali.
