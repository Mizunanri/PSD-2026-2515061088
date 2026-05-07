Sistem Pencarian Data Pasien Menggunakan Sequential Search
===================================================================

A. Judul Program
================
Program sistem Pencarian Data Pasien Menggunakan Sequential Search

B. Deskripsi Singkat
====================

Program ini dibuat untuk mencari data pasien rumah sakit menggunakan algoritma Sequential Search. Program bekerja dengan cara memeriksa data pasien satu per satu hingga nama pasien yang dicari ditemukan.

Pada program ini, pengguna dapat mencari nama pasien kemudian program akan menampilkan informasi berupa ruangan rawat inap dan status pasien. Algoritma Sequential Search dipilih karena mudah dipahami dan cocok digunakan pada data sederhana yang tidak harus terurut.


C. Penjelasan Kode
==================

    def sequential_search(data, n, target):
        i = 0
        while i < n:
            if data[i].lower() == target.lower():
                return i
            i += 1
        return -1
membuat fungsi pencarian sequential dengan parameter data, n, dan target 
lalu membuat index 0 untuk mencari data dari awal
kemudian mengguanakan looping while dengan syarat jika 1 lebih kecil dari n maka 
if data index 0 = target yang dicari maka mengembalikan nilai yg benar ke indek(i)
jika belum maka index yang tadi 0 +1
jikalau masih belum ketemu maka mengembalikan -1

    def main():
        data = [
            "Natalyn",
            "Amuro",
            "Cynthia",
            "Ash",
            "Kafka"
        ]
        ruangan = [
            "Mawar-01",
            "Anggrek-05",
            "Melati-01",
            "Flamboyan-02",
            "Tulip-04"
        ]
        status = [
            "Operasi",
            "Pemulihan",
            "Rawat Inap",
            "Pemulihan",
            "Rehabilitasi"
        ]
        n = len(data)
selanjutnya memulai fungsiutama sistem yang mana dimulai dengan menambahkan list dari 3 hal yaitu nama pasien, ruangan, dan status pasien yang menginap, lalu n untuk mengukur panjang dari data pasien yg berfungsi sebagai pembanding data, jadi jika  panjang data 5 maka melakukan searching dari index 0 sampai index terakhir

    print("=== Sistem Pencarian Data Pasien ===")
    print(f"Data pasien : {data}")
    target = input("Masukkan nama pasien yang dicari: ")
    posisi = sequential_search(data, n, target)
kemudian melakukan cetak dari sistem dan penginputan nama pasien yang mau dicari
kemudian pasien yang mau dicari sebagai target akan memicu posisi yang mana melakukan fungsi sequential_search dan melakukan pencarian target dari index awal hingga akhir

    if posisi != -1:

        print("\nData pasien ditemukan")
        print(f"Nama pasien        : {data[posisi]}")
        print(f"Tempat rawat inap  : {ruangan[posisi]}")
        print(f"Status pasien      : {status[posisi]}")

    else:
        print("\nData pasien tidak ditemukan")
lalu jika sudah melakukan search maka menentukan kondisi jika posisi != -1 yang mana pasien ketemu maka melakukan perint pasien ditemukan lalu cetak nama, letak ruangan, dan status pasien yang menginap

jika tidak ketemu maka return -1 yang mana melakukan print data pasien tidak ditemukan

    if __name__ == "__main__":
        main()
terakhir adalah untuk memulai program secara keseluruhan dari awal hingga akhir

D. Output Program
=================

    foto 1
Sistem dibuka dengan nama sistem pencarian data pasien dan melakukan input nama pasien yang mau dicari sebagai target

    foto 2
jika data yang dicari ditemukan maka akan melakukan print data ditemukan lalu mencetak nama pasien yang dicari beserta ruangan dan status kondisi pasien

    foto 3
dan jika data yang dicari tidak ditemukan maka akan melakukan print Data pasien tidak ditemukan

e. Link YouTube
===============
Link Video Demo:
(https://youtu.be/bwCw3dYOZcA)

Kesimpulan
==========

Program Sistem Pencarian Data Pasien menggunakan Sequential Search berhasil dibuat dan dijalankan dengan baik. Program dapat mencari nama pasien secara berurutan dari awal hingga data ditemukan, kemudian menampilkan informasi berupa ruangan rawat inap dan status pasien.

Dari program ini dapat dipahami bahwa algoritma Sequential Search merupakan metode pencarian yang sederhana dan mudah diterapkan pada data sederhana. Meskipun proses pencarian dilakukan satu per satu, tapi tetap efektif digunakan pada jumlah data yang tidak terlalu besar.
