# Tugas 3 PBP - Create ToDo List

Link Heroku : 

## Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?

`{% csrf_token %}` merupakan random string di mana setiap halaman yang berisi form, maka token tersebut di-generate di server-side daat halaman di-render dan akan mengecek dari semua request yang masuk. CSRF Token ini dapat mencegah serangan CSRF (Cross-Site Request Forgery) yang akan membuat penyerang tidak mungkin melakukan permintaan HTTP yang secara sepenuhnya valid yang cocok untuk diumpankan ke pengguna korban. Caranya token ini bekerja, ialah token ini akan meng-compare pada saat pengguna memasuki laman `<form>` dan pada setelah request dikembalikan dari pengguna saat men-submit data yang dibutuhkan pada `<form>`. Setelah itu, kedua token akan di-compare, dan jika sama maka request tersebut akan dikembalikan.

Yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>` ialah bisa saja berjalan pad wesbite, tetapi bisa muncul kemungkinan error, yaitu `Forbidden (403) CSRF verification failed` dikarenakan ketidakcocokan pada kedua token.

## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Benar, kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }}) yaitu dengan menggunakan method `POST`. Untuk hal ini juga dibutuhkan kembali `{% csrf_token %}`. Caranya ialah dengan membuat method `POST` tersebut dan diberikan token, membuat tag table dan memasukan tag `<input>` yang berguna untuk pengisian form, dan tidak lupa untuk memberi nama sebagai identifier. Tidak lupa untuk menambahkan <input type="submit"> untuk meng-submit form tersebut. Setlah disubmit, nantinya kita dapat mengakses input yang dimasukkan melalui method `get.POST`.

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Pengguna mengisi submisi yang ada pada HTML. Dalam HTML tersebut akan merender dan mensubmit setekah pengguna menekan tombol submit. Pada `views.py` terdapat function yang bertugas untuk meng-handle  dan meneglola kejadian tersebut. Jika ada perubahan data (mengganti status pada aplikasi todolist misalnya), maka perubahan tersebut akan disimpan sementara jika ada data baru yang dibuat oleh pengguna, maka akan meng-create objek baru dan disimpan pada database. Setelah itu, data-data akan terlihat pada HTMl setelah proses rendering.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
- Membuat aplikasi `todolist` dengan cara menjalankan command `python manage.py startapp todolist`.
- Menambahkan aplikasi todolist ke dalam installed apps pada folder `prodject django` serta menambahkan `path('todolist/', include('todolist.urls'))` pada `urls.py`.
- Pada folder `todolist`, kita membuat model `Task` dengan parameter models.Model dan memasukan data apa saja yang dibutuhkan (seperti user, date, title, description) dengan field yang sesuai.
- Membuat function untuk login, logout, dan resgiter pada `views.py` pada folder todolist (`login_user`, `logout_user`, dan `register`). Adapun membuat template HTML, yaitu todolist.html untuk tampilan utamanya
- Membuat template HTMl yaitu `create-task.html` untuk memasukan input pepmbuatan task yang berisi judul dan deskripsi
- Melakukan routing pada urls.py di folder `todolist` agar terlihat pada website.
- Melakukan deployment dengan cara push ke Github.
- Membuat dua akun dan tiga dummy data dengan cara membuat akun pada `http://localhost:8000/todolist/register` dan membuat dummy task pada `http://localhost:8000/todolist/create-task`