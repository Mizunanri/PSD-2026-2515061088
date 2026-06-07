Sistem Manajemen Stok Obat Apotek Menggunakan Hash Map Separate Chaining
========================================================================

A. Judul Program
================
Sistem Manajemen Stok Obat Apotek Menggunakan Hash Map Separate Chaining

B. Deskripsi Singkat
====================

Program ini merupakan sistem sederhana untuk mengelola stok obat pada sebuah apotek menggunakan struktur data Hash Map dengan metode Separate Chaining. Setiap obat memiliki kode obat yang digunakan sebagai key dan jumlah stok sebagai value. Struktur data Hash Map dipilih karena mampu melakukan pencarian data dengan cepat berdasarkan kode obat.

Metode Separate Chaining digunakan untuk mengatasi collision yang terjadi ketika beberapa key menghasilkan indeks hash yang sama. Program ini menyediakan fitur menambah data obat, mencari data obat, mengubah stok obat, dan menghapus data obat. Dengan demikian pengelolaan data stok obat menjadi lebih mudah dan efisien.


C. Penjelasan Kode
==================

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/ade11c926ce2c9a67a1eab2ecc4420fbaee91c6e/img6/Screenshot%202026-06-07%20170453.png)

    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None
pertama membuat objek/class node tree dengan fungsi dengan parameter self, key dan value
self berfungsi memanggil diri sendiri lalu untuk key untuk inisiasi nlai dari value dan memanggil nilai value, dan value untuk nilai dari key

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/ade11c926ce2c9a67a1eab2ecc4420fbaee91c6e/img6/Screenshot%202026-06-07%20170512.png)

    class HashMapSeparateChaining:
        def __init__(self, size=10):
            self.SIZE = size
            self.table = [None] * self.SIZE
            
        def hash_function(self, key):
            return (key % self.SIZE + self.SIZE) % self.SIZE
selanjutnya memulai dengan buat class hash map separate Chaining dan pemanggilan fungsi membuat table dengan ukuran 10 yg mana masih kosong dan function untuk memastikan saja hash map berkerja atau tidak serta menentukan posisi (indeks) penyimpanan data pada Hash Map berdasarkan kode obat yang dimasukkan. 

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/ade11c926ce2c9a67a1eab2ecc4420fbaee91c6e/img6/Screenshot%202026-06-07%20170520.png)

        def insert(self, key, value):
            index = self.hash_function(key)
            current = self.table[index]
            while current is not None:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            new_node = Node(key, value)
            new_node.next = self.table[index]
            self.table[index] = new_node

        def search(self, key):
            index = self.hash_function(key)
            current = self.table[index]
            while current is not None:
                if current.key == key:
                    return current
                current = current.next
            return None

kemudian fungsi insert dimulai dengan mengisi index dan current untuk cek apakah key nilainya kosong atau tidak, jika tidak maka ke dan value yg diinputkan akan masuk kedalam current saat ini dan current berpindah ke node baru, kalau ada maka current adak indexnya akan berpindah ke node baru yang sudah dipindahkan saat terakhir melakukan insert.

selanjutnya ada search sama seperti insert tetapi fungsinya untuk mencari suatu value berdasarkan key yg diinputkan.

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/ade11c926ce2c9a67a1eab2ecc4420fbaee91c6e/img6/Screenshot%202026-06-07%20170533.png)

        def update_stock(self, key, stok_baru):
            hasil = self.search(key)
            if hasil is not None:
                hasil.value = stok_baru
                return True
            return False

        def delete(self, key):
            index = self.hash_function(key)
            current = self.table[index]
            prev = None
            while current is not None:
                if current.key == key:
                    if prev is None:
                        self.table[index] = current.next
                    else:
                        prev.next = current.next
                    return True
                prev = current
                current = current.next
            return False
lanjut ke update stok dimulai dari hasil yg mana menggunakan fungsi search untuk mencari key mana yg nilainya mau diubah kemudian valuenya diganti dengan value baru.

terakhir fungsi delete karena fungsinya mirip kaya linked list jadi prev akan mulai dri luar dan current di key awal jika nilainya bukan itu maka prev dan current akan pindah kedepan, jika data yg mau  dihapus sudah sesuai maka curent akan dilewat dan prev akan maju kedepan dan current akan berpindah posisi sehingga current pindah ke prev bagian depan dan prev akan berpindah ke tempat semula sebelum data yg dihapus.

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/ade11c926ce2c9a67a1eab2ecc4420fbaee91c6e/img6/Screenshot%202026-06-07%20170546.png)

    def main():
        hashmap = HashMapSeparateChaining()
        pilih = 0
        while pilih != 5:
            print("\n=== SISTEM STOK OBAT APOTEK ===")
            print("1. Tambah Obat")
            print("2. Cari Obat")
            print("3. Edit Stok Obat")
            print("4. Hapus Obat")
            print("5. Keluar")
            pilih = input("Pilih menu: ")
nah masuk ke main program dmn ini dimulai dgn membuat fungsi hash map dan sistem stok obatnya, jika memilih 1-5 maka bisa melakukan sesuai kebutuhan kalau tidak dari 1-5 maka akan tidak valid.

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/ade11c926ce2c9a67a1eab2ecc4420fbaee91c6e/img6/Screenshot%202026-06-07%20170623.png)

            if pilih == "1":
                try:
                    kode = int(input("Masukkan kode obat : "))
                    stok = int(input("Masukkan stok obat : "))
                    if hashmap.search(kode) is not None:
                        print("Kode obat sudah terdaftar!")
                    else:
                        hashmap.insert(kode, stok)
                        print("Data obat berhasil ditambahkan")
                except ValueError:
                    print("Input harus berupa angka!")
            elif pilih == "2":
                try:
                    kode = int(input("Masukkan kode obat : "))
                    hasil = hashmap.search(kode)
                    if hasil is not None:
                        print(f"Kode Obat : {hasil.key}")
                        print(f"Stok Obat : {hasil.value}")
                    else:
                        print("Obat tidak ditemukan")
                except ValueError:
                    print("Input harus berupa angka!")
            elif pilih == "3":
                try:
                    kode = int(input("Masukkan kode obat : "))
                    stok_baru = int(input("Masukkan stok baru : "))
                    if hashmap.update_stock(kode, stok_baru):
                        print("Stok obat berhasil diperbarui")
                    else:
                        print("Obat tidak ditemukan")
                except ValueError:
                    print("Input harus berupa angka!")
            elif pilih == "4":
                try:
                    kode = int(input("Masukkan kode obat yang akan dihapus : "))
                    if hashmap.delete(kode):
                        print("Data obat berhasil dihapus")
                    else:
                        print("Obat tidak ditemukan")
                except ValueError:
                    print("Input harus berupa angka!")
            elif pilih == "5":
                print("Program selesai.")
            else:
                print("Pilihan tidak valid!")

ini adalah bbrp kondisi dari 5 fungsi utama sistem

            if pilih == "1":
                try:
                    kode = int(input("Masukkan kode obat : "))
                    stok = int(input("Masukkan stok obat : "))
                    if hashmap.search(kode) is not None:
                        print("Kode obat sudah terdaftar!")
                    else:
                        hashmap.insert(kode, stok)
                        print("Data obat berhasil ditambahkan")
                except ValueError:
                    print("Input harus berupa angka!")
ini fungsi insert yg mana melakukan input kode dan stok jika belum ada maka akan ditambahkan jika belum akan dibu=ilang sudah ditambahkan, kalau bukan int maka disuruh input berupa angka.

            elif pilih == "2":
                try:
                    kode = int(input("Masukkan kode obat : "))
                    hasil = hashmap.search(kode)
                    if hasil is not None:
                        print(f"Kode Obat : {hasil.key}")
                        print(f"Stok Obat : {hasil.value}")
                    else:
                        print("Obat tidak ditemukan")
                except ValueError:
                    print("Input harus berupa angka!")

ini menu 2 sama seperti insert tetapi ini mencari key dan value jika tidak ditemukan maka print obat tidak ditemukan dan jika bukan int maka muncul pesan input harus angka.

            elif pilih == "3":
                try:
                    kode = int(input("Masukkan kode obat : "))
                    stok_baru = int(input("Masukkan stok baru : "))
                    if hashmap.update_stock(kode, stok_baru):
                        print("Stok obat berhasil diperbarui")
                    else:
                        print("Obat tidak ditemukan")
                except ValueError:
                    print("Input harus berupa angka!")
lanjut ke opsi 3 sama seperti 1 dan 2 tapi ini akan merubah stok lama key jadi value baru jika key tidak ditemukan maka ada pesan tidak ditemukan.

            elif pilih == "4":
                try:
                    kode = int(input("Masukkan kode obat yang akan dihapus : "))
                    if hashmap.delete(kode):
                        print("Data obat berhasil dihapus")
                    else:
                        print("Obat tidak ditemukan")
                except ValueError:
                    print("Input harus berupa angka!")
ada juga 4 yg mana mencari kode yaitu key jika ketemu maka otomatis terhapus.

            elif pilih == "5":
                print("Program selesai.")
                break
            else:
                print("Pilihan tidak valid!")
dan masih ada 5 yg mana malakukan print program selesai dan sistem berhenti. 

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/ade11c926ce2c9a67a1eab2ecc4420fbaee91c6e/img6/Screenshot%202026-06-07%20170645.png)

    if __name__ == "__main__":
        main()
nah terakhir ada untuk memulai program dari awal hingga akhir

D. Output Program
=================

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/bee10d7f0930f1f89b64a584c340b3735dffd363/img6/Screenshot%202026-06-07%20203356.png)

Sistem dibuka dengan memilih dari 5 pilihan menu

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/ade11c926ce2c9a67a1eab2ecc4420fbaee91c6e/img6/Screenshot%202026-06-07%20192838.png)

pertama memasukan kode obat dan stoknya

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/ade11c926ce2c9a67a1eab2ecc4420fbaee91c6e/img6/Screenshot%202026-06-07%20192851.png)

misal disini salah input kode obat maka akan tidak ditemukan

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/ade11c926ce2c9a67a1eab2ecc4420fbaee91c6e/img6/Screenshot%202026-06-07%20192902.png)

lanjut update stok dengan cari kode obat dan akan  diminta untuk stok terbaru

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/ade11c926ce2c9a67a1eab2ecc4420fbaee91c6e/img6/Screenshot%202026-06-07%20192930.png)

lanjut update stok dengan cari kode obat dan akan  diminta untuk stok terbaru

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/ade11c926ce2c9a67a1eab2ecc4420fbaee91c6e/img6/Screenshot%202026-06-07%20192953.png)

kalau menghapus maka saat dicari akan tidak ditemukan karna sudah diremove

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/ade11c926ce2c9a67a1eab2ecc4420fbaee91c6e/img6/Screenshot%202026-06-07%20193119.png)

kalau kamu salah memilih pilihan menu maka akan tidak valid

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/ade11c926ce2c9a67a1eab2ecc4420fbaee91c6e/img6/Screenshot%202026-06-07%20193144.png)

terakhir 5 untuk mengakhiri sistem

e. Link YouTube
===============
Link Video Demo:
(https://youtu.be/xS08Y-8pAJU)

Kesimpulan
==========

Program Sistem Manajemen Stok Obat Apotek berhasil menerapkan struktur data Hash Map dengan metode Separate Chaining untuk menyimpan dan mengelola data stok obat. Struktur data ini memungkinkan proses pencarian, penambahan, perubahan, dan penghapusan data dilakukan dengan lebih cepat dan efisien.

Melalui implementasi ini dapat dipahami bahwa Hash Map sangat cocok digunakan pada sistem yang membutuhkan akses data berdasarkan kode atau identitas tertentu, seperti sistem persediaan obat pada apotek.
