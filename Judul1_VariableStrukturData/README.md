Program Kasir Sederhana (List 1D)

a. Judul Program
=================================
Program Kasir Sederhana Menggunakan Struktur Data List 1 Dimensi

b. Deskripsi Singkat
====================

Program ini dibuat untuk mensimulasikan sistem kasir sederhana menggunakan bahasa Python. Di dalam program ini, pengguna bisa menambahkan barang ke dalam keranjang, melihat daftar barang yang sudah dimasukkan, menghapus barang tertentu jika tidak jadi dibeli, dan melakukan proses pembayaran.

Struktur data yang digunakan adalah list 1 dimensi, yaitu dengan menggunakan dua buah list. List pertama digunakan untuk menyimpan nama barang (keranjang), sedangkan list kedua digunakan untuk menyimpan harga barang (harga). Kedua list ini saling berhubungan berdasarkan index, jadi data tetap konsisten. Dengan cara ini, program bisa mengelola data secara sederhana tapi tetap rapi.


c. Penjelasan Kode
==================

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/4aba12bb568b328f6e1d62588caa2d881a3890b7/img/Screenshot%202026-04-28%20143744.png)

   def main():
Baris ini digunakan untuk mendefinisikan fungsi utama program.

      keranjang = []
      harga = []

Membuat dua list kosong:
-keranjang untuk menyimpan nama barang
-harga untuk menyimpan harga barang


![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/3db43704a95f62a618227392b54136329efb0a26/img/Screenshot%202026-04-28%20143806.png)

    while True:
Perulangan ini digunakan agar program terus berjalan sampai pengguna memilih keluar.

        print("\nMenu:")
        print("1. Tambah Barang")
        print("2. Tampilkan Keranjang")
        print("3. Hapus Barang")
        print("4. Bayar")
        print("5. Keluar")
Menampilkan daftar menu yang bisa dipilih oleh pengguna.

        pilihan = input("Pilih menu: ")
Menyimpan input pilihan menu dari pilihan si pengguna.

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/3db43704a95f62a618227392b54136329efb0a26/img/Screenshot%202026-04-28%20143825.png)

        if pilihan == "1":
            nama = input("Masukkan nama barang: ")
            hrg = int(input("Masukkan harga barang: ").replace(".", ""))
            keranjang.append(nama)
            harga.append(hrg)
kondisi dimana memilih menu 1 :
-Menginput nama-nama barang
-Menginput harga lalu mengubahnya jadi integer
-replace(".", "") digunakan agar input seperti 10.000 tetap bisa dibaca
-Menyimpan data ke dalam masing-masing list keranjang dan harga menggunakan   append()


![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/3db43704a95f62a618227392b54136329efb0a26/img/Screenshot%202026-04-28%20143842.png)


        elif pilihan == "2":
            if len(keranjang) == 0:
                print("Keranjang kosong")
elif atau kondisi lain yang mana ini pilihan untuk menu 2
menggunakan if-else untuk mengecek apakah keranjang kosong atau tidak dengan len() yang mana untuk menghitung jumlah elemen.

            else:
                print("\nIsi Keranjang:")
                for i in range(len(keranjang)):
                    print(f"{i+1}. {keranjang[i]} - Rp{harga[i]}")
-kodisi else dimana jika tidak kososng maka menggunakan perulangan for untuk menampilkan semua isi list
-i+1 digunakan agar nomor mulai dari 1 dan

    {keranjang[i]} - Rp{harga[i]}
menampilkan nama barang serta harganya.


![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/3db43704a95f62a618227392b54136329efb0a26/img/Screenshot%202026-04-28%20143907.png)

        elif pilihan == "3":
            if len(keranjang) == 0:
                print("Keranjang kosong")
elif atau pilihan kondisi memilih menu 3
Cek apakah keranjang kosong jika iya maka print "Keranjang kosong" jika tidak maka ke kondisi selanjutnya

            else:
                for i in range(len(keranjang)):
                    print(f"{i+1}. {keranjang[i]} - Rp{harga[i]}")

Menggunakan looping for dan len(keranjang) supaya bisa menampilkan daftar barang agar user bisa memilih .

              try:
                  jumlah = int(input("Berapa barang yang ingin dihapus? "))
              except ValueError:
                  print("Input tidak valid")
                  continue
menggunakan try dan except untuk user menentukan berapa banyak barang yang ingin dihapus menggunakan input jumlah dan tipe data integer atau hanya bilangan bulat, jika jumlay yg dimasukkan bukan integer atau tidak sesuai maka akan tidak valid.

                for _ in range(jumlah):
Loop for sesuai jumlah barang yang akan dihapus.

                    try:
                        idx = int(input("Pilih nomor barang yang dihapus: ")) - 1
Mengambil input nomor barang dan mengubahnya ke index.

                        if 0 <= idx < len(keranjang):
menggunakan validasi if agar index tidak keluar dari batas list.

                            print(f"{keranjang[idx]} dihapus")
                            keranjang.pop(idx)
                            harga.pop(idx)
jika sesuai maka menapilkan index keranjang yang akan dihapus dan menghapus data dari kedua list agar tetap sinkron.

                        else:
                            print("Index tidak valid")
Jika nomor tidak sesuai maka "Index tidak valid".

                    except ValueError:
                        print("Input tidak valid")
karena try membuat idx dengan tipe integer jika yang dimasukan bukan tipe yg sesuai maka error jika input bukan angka.


![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/3db43704a95f62a618227392b54136329efb0a26/img/Screenshot%202026-04-28%20143928.png)

        elif pilihan == "4":
            if len(keranjang) == 0:
                print("Keranjang kosong, tidak bisa bayar")
elif jika user memasukan angka pilihan menu 4 dan if untuk cek apakah ada barang untuk dibayar, jika 0 maka tidak bisa bayar.

            else:
                total = sum(harga)
                print(f"Total belanja = Rp{total}")
Menjumlahkan semua harga menggunakan sum()
menampilkan total belanja berserta harga total.

                bayar = int(input("Masukkan uang bayar: ").replace(".", ""))
Mengambil input uang dari user, replace jika user memasukan nilai "10.000" maka tidak eror dan memunculkan 10000.

                if bayar < total:
                    print("Uang tidak cukup")

Cek apakah uang cukup jika tidak maka print "Uang tidak cukup".

                else:
                    kembalian = bayar - total

jika cukup atau lebih maka menghitung kembalian.

                    print("\n===== KWITANSI =====")

Menampilkan struk pembelian.

                    for i in range(len(keranjang)):
                        print(f"{i+1}. {keranjang[i]} - Rp{harga[i]}")

Menampilkan daftar barang yang dibeli.

                    print("-------------------")
                    print(f"Total = Rp{total}")
                    print(f"Bayar = Rp{bayar}")
                    print(f"Kembalian = Rp{kembalian}")
                    print("===================")

Menampilkan total, uang bayar, dan kembalian.

                    keranjang.clear()
                    harga.clear()

Mengosongkan data setelah transaksi selesai dengan menghapus isi dari kedua list.


![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/3db43704a95f62a618227392b54136329efb0a26/img/Screenshot%202026-04-28%20143942.png)

        elif pilihan == "5":
            print("Terima kasih")
            break

Memilih opsi 5 pada menu maka mencetak "Terima kasih" lalu menghentikan program dengan break.


![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/3db43704a95f62a618227392b54136329efb0a26/img/Screenshot%202026-04-28%20143953.png)

        else:
            print("Pilihan tidak valid")

jika memengetik pilihan/no yg tidak ada dimenu if dan elif jika input menu salah karna opsinya hanya 1-5 jika tidak dari nomor itu maka menampilkan pesan "Pilihan tidak valid".


![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/3db43704a95f62a618227392b54136329efb0a26/img/Screenshot%202026-04-28%20144001.png)

    if __name__ == "__main__":
      main()

Menjalankan fungsi utama program kasir sederhana.

d. Output Program
=================


![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/3db43704a95f62a618227392b54136329efb0a26/img/Screenshot%202026-04-28%20175210.png)
sistem dimulai dengan pilihan menu dari program kasir dan input untuk pilihan menu


![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/3db43704a95f62a618227392b54136329efb0a26/img/Screenshot%202026-04-28%20180151.png)

saat pilihan tambah barang maka menginputkan nama barang dan harganya contohnya Pocari Sweat 2L dengan harga 22.000


![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/3db43704a95f62a618227392b54136329efb0a26/img/Screenshot%202026-04-28%20180000.png)

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/3db43704a95f62a618227392b54136329efb0a26/img/Screenshot%202026-04-28%20175949.png)

kita menambahkan 2 belanjaan lainnya seperti Mi sedap soto koya dengan harga 4.500 dan mi indomie goreng jumbo dengan harga 6.000


![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/3db43704a95f62a618227392b54136329efb0a26/img/Screenshot%202026-04-28%20180736.png)

kalau kamu memilih menu 2 yaitu tampilkan keranjang maka sistem akan menampilkan berang belanjaanmu serta harga dari setiap barang


![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/3db43704a95f62a618227392b54136329efb0a26/img/Screenshot%202026-04-28%20180920.png)

jika kamu mau menghapus salah satu atau lebih barang belanjaan maka pilih opsi 3, maka sistem akan menapilkan input untuk menentukan berapa banyak barang yg ingin dihapus 


![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/3db43704a95f62a618227392b54136329efb0a26/img/Screenshot%202026-04-28%20181526.png)

misal kita mau menghapus indomie goreng jumbo maka saat tampilkan belanjaan maka indomie goreng jumbo akan hilang dari daftar belanjaan


![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/3db43704a95f62a618227392b54136329efb0a26/img/Screenshot%202026-04-28%20182024.png)

pada saat memilih opsi menu bayar maka akan memunculkan total daari harga barang yang hendak mau dibeli, lalu kita akan memasukkan uang kita

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/3db43704a95f62a618227392b54136329efb0a26/img/Screenshot%202026-04-28%20182233.png)

jika uang yang dimasukkan kurang maka akan menampilkan uang tidak cukup dan program akan mengulakan ke opsi pemilihan

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/3db43704a95f62a618227392b54136329efb0a26/img/Screenshot%202026-04-28%20182423.png)


jika memasukan uang yg cukup maka akan menampilkan kwitansi, apabila uang yg dibayar lebih maka akan muncul total kembalian dari belanjaan, misal kita membayar belanjaan 26.500 dengan uang 27.000 maka akan ada kembalian Rp500

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/3db43704a95f62a618227392b54136329efb0a26/img/Screenshot%202026-04-28%20182803.png)

jika kita memilih opsi 5 yaitu keluar maka akan muncul pesan Terima kasih dan program kasir sederhana berhenti otomatis

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/3db43704a95f62a618227392b54136329efb0a26/img/Screenshot%202026-04-28%20175936.png)

jika pilihan yang kita masukan tidak benar maka akan muncul pesan pilihan tidak valid dan program kan melakukan pemilihan ulang

e. Link YouTube
===============
Link Video Demo:
(https://youtu.be/bwCw3dYOZcA)

Kesimpulan
==========
Program ini berhasil mengimplementasikan struktur data List 1 Dimensi dalam studi kasus kasir sederhana. Penggunaan list memungkinkan pengelolaan data yang fleksibel dan mudah, terutama dalam operasi penambahan, penghapusan, dan pencarian data.
