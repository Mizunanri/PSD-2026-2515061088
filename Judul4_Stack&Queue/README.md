Sistem Antrean Richeese Factory Menggunakan Queue Array
=======================================================

A. Judul Program
================
Sistem Antrean Richeese Factory Menggunakan Queue Array

B. Deskripsi Singkat
====================

Program ini dibuat untuk mensimulasikan sistem antrean pelanggan di Richeese Factory menggunakan struktur data Queue Array. Sistem antrean bekerja dengan konsep FIFO (First In First Out), yaitu pelanggan yang datang lebih dahulu akan dilayani lebih dahulu.

Pada program ini pelanggan dapat mengambil nomor antrean, melihat antrean terdepan, memanggil antrean pelanggan, serta menampilkan seluruh daftar antrean. Struktur data Queue Array dipilih karena sangat cocok digunakan pada sistem antrean yang berjalan secara berurutan sesuai dari Queue itu sendiri.


C. Penjelasan Kode
==================

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/baa59d1de519b27f3a59a631f4781791af6bc3a9/img4/Screenshot%202026-05-15%20075432.png)

    class QueueArray:
        def __init__(self, max_size=100):
            self.MAXN = max_size
            self.q = [None] * self.MAXN
            self.front_idx = -1
            self.rear_idx = -1

        def is_empty(self):
            return self.front_idx == -1

        def is_full(self):
            return (self.rear_idx + 1) % self.MAXN == self.front_idx
pertama buat fungsi QueueArray dan dalamanya memuat beberapa fungsi kayak fungsi queue dlu dimulai dari menambah parameter self, dan max_size dgn ukuran 100(sesuai kebutuhan)
lalu membuat ukuran max_size sama dengan maxn kemudian self.q membuat 100 none karna array masih kosong dan self rear dan front -1 karna tidak dibawah nol

lanjut membuat 2 fungsi lain seperti is_empty dengan mengembalikan index depan = -1 
dan is_full dengan kembalikan fungsi self.rear_idx + 1 mod dari self.MAXN == self.front_idx jika rear mod nilai max=front maka fungsi is_full akan aktif

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/baa59d1de519b27f3a59a631f4781791af6bc3a9/img4/Screenshot%202026-05-15%20075448.png)

    def enqueue(self, nilai):

        if self.is_full():
            print("Antrean penuh")
            return

        if self.is_empty():
            self.front_idx = 0
            self.rear_idx = 0

        else:
            self.rear_idx = (self.rear_idx + 1) % self.MAXN

        self.q[self.rear_idx] = nilai

        print(f"Nomor antrian {nilai} ditambahkan")
selanjutnya memulai enque dengan cek apakah antrian full atau kosong dan jika tidak keduanya maka memanggil else dengan memasukan nilai kedalam index self_rear lalu dimasukan ke nilai

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/baa59d1de519b27f3a59a631f4781791af6bc3a9/img4/Screenshot%202026-05-15%20075504.png)

    def dequeue(self):

        if self.is_empty():
            print("Antrean kosong")
            return

        print(f"Nomor antrian {self.q[self.front_idx]} silakan mengmbil makanan di kasir")

        if self.front_idx == self.rear_idx:
            self.front_idx = -1
            self.rear_idx = -1

        else:
            self.front_idx = (self.front_idx + 1) % self.MAXN
kemudian dequeue dengan cek apakah kosong jika tidak maka print Nomor antrian {self.q[self.front_idx]} silakan mengmbil makanan di kasir lanjut dengan if index depan=index belakang maka keduanya dianggap kosong(-1) jika tidak sama maka else memanggil index setelahnya kedepan

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/baa59d1de519b27f3a59a631f4781791af6bc3a9/img4/Screenshot%202026-05-15%20075517.png)

    def peek(self):

        if self.is_empty():
            print("Antrean kosong")
            return

        print(f"Antrean terdepan: {self.q[self.front_idx]}")

    def display(self):

        if self.is_empty():
            print("Antrean kosong")
            return

        print("Daftar antrean Richeese: ", end="")

        i = self.front_idx

        while True:
            print(self.q[i], end=" ")

            if i == self.rear_idx:
                break

            i = (i + 1) % self.MAXN

        print()
lanjut ke peek dengan cek apakah kosong jika tidak maka print index antrian depan
dan fungsi terakhir display yg mana cek apakah kosong jika tidak maka akan melakukan print antrian dari depan hingga belakang

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/baa59d1de519b27f3a59a631f4781791af6bc3a9/img4/Screenshot%202026-05-15%20075633.png)

    def main():
        queue = QueueArray()
        pilih = 0
        while pilih != 5:
            print("\n=== ANTREAN RICHEESE FACTORY ===")
            print("1. Ambil Antrean")
            print("2. Panggil Antrean")
            print("3. Lihat Antrean Depan")
            print("4. Tampilkan Semua Antrean")
            print("5. Keluar")
            try:
                pilih = int(input("Pilih menu: "))
            except ValueError:
                print("Input tidak valid!")
                continue
nah masuk ke fungsi programnya dengan memangil fungsi queue array dan pilih=0
kemudian if jika pilih tidak sama dengan 5 maka print pilihan fungsi
lanjut ada try input pilihan menu jika yg diinput bukan integer maka print input tdk valid dan program dilanjutkan

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/baa59d1de519b27f3a59a631f4781791af6bc3a9/img4/Screenshot%202026-05-15%20075708.png)

            if pilih == 1:
                nomor = input("Masukkan nomor antrean: ")
                queue.enqueue(nomor)
            elif pilih == 2:
                queue.dequeue()
            elif pilih == 3:
                queue.peek()
            elif pilih == 4:
                queue.display()
            elif pilih == 5:
                print("Program selesai")
            else:
                print("Pilihan tidak valid!")

    if __name__ == "__main__":
        main()
kemudian ada if yg mana dri 1-5 memuat seluruh fungsi mulai enqueue,dequeue,peek,display,dan exit yg mana diakhiri denga print program selesai
jika yg diinput bukan 1-5 maka print tidak valid

dan terakhir if main yg mana memulai keseluruhan dari program 

D. Output Program
=================

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/baa59d1de519b27f3a59a631f4781791af6bc3a9/img4/Screenshot%202026-05-15%20082844.png)

Sistem dibuka dengan nama sistem pencarian data pasien dan melakukan input dari 5 pilihan

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/baa59d1de519b27f3a59a631f4781791af6bc3a9/img4/Screenshot%202026-05-15%20082930.png)

jika milih 1 maka akan menambahkan data keantrian contoh disini menambah kan data antrian nomor 1-3

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/baa59d1de519b27f3a59a631f4781791af6bc3a9/img4/Screenshot%202026-05-15%20082950.png)

dan jika data ditampilkan maka bisa dilihat data dicetak dri awal hingga akhir antrian

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/baa59d1de519b27f3a59a631f4781791af6bc3a9/img4/Screenshot%202026-05-15%20083005.png)

jika kita memilih menu 3 maka kita bisa melihat atrian paling depan

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/baa59d1de519b27f3a59a631f4781791af6bc3a9/img4/Screenshot%202026-05-15%20083214.png)

jika mau dequeue atau pilihan 2 maka otomatis antrian depan seperti 1 akan hilang jika dilihat antrian 1 sudah ridak ada dan hanya antrian 2 dan 3


![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/baa59d1de519b27f3a59a631f4781791af6bc3a9/img4/Screenshot%202026-05-15%20083959.png)

jika 5 maka print program selesai dan sistem berakhir

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/baa59d1de519b27f3a59a631f4781791af6bc3a9/img4/Screenshot%202026-05-15%20083934.png)

jika tidak menginput selain 1-5 maka akan print input tidak valid 

e. Link YouTube
===============
Link Video Demo:
(https://youtu.be/bwCw3dYOZcA)

Kesimpulan
==========

Program Sistem Antrean Richeese Factory menggunakan Queue Array berhasil dibuat dan dijalankan dengan baik. Program dapat digunakan untuk menambahkan antrean pelanggan, memanggil antrean, melihat antrean terdepan, dan menampilkan seluruh antrean.

Dari program ini dapat dipahami bahwa struktur data Queue sangat cocok digunakan pada sistem antrean karena menggunakan konsep FIFO (First In First Out), yaitu data yang masuk lebih dahulu akan dilayani lebih dahulu.
