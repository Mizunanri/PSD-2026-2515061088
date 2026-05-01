A. Judul Program
================
Program Pengurutan Nama Mahasiswa Menggunakan Algoritma Bubble Sort

B. Deskripsi Singkat
====================

Program ini dibuat untuk mengurutkan data nama mahasiswa menggunakan algoritma Bubble Sort.
Pengurutan dilakukan secara ascending (A-Z) berdasarkan abjad dan kapital tidak mempengaruhi karena pengurutan huruf sesuai urutan.

Algoritma Bubble Sort bekerja dengan cara membandingkan dua elemen yang bersebelahan, kemudian menukarnya jika urutan tidak sesuai.
Proses ini dilakukan berulang hingga seluruh data terurut dengan benar.

C. Penjelasan Kode
==================

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/1984b9ef4fbae57e2d2dc17b372e111a093ab511/img2/Screenshot%202026-05-01%20153920.png)


    def tukar(arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
disini fungsi tukar yg mana berfungsi untuk melakukan penukaran variable sorting
temp untuk menyimpan sementara data dan arr[i], arr[j] itu tempat dari data yang mau diurutkan(sorting)

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/1984b9ef4fbae57e2d2dc17b372e111a093ab511/img2/Screenshot%202026-05-01%20153932.png)

    def bubble_sort(arr, n):
        for i in range(n - 1):
            for j in range(n - i - 1):
                if arr[j].lower() > arr[j + 1].lower():
                    tukar(arr, j, j + 1)
ini adalah programyang digunakan yaitu bubble_sort, sort ini berfungsi mengurutkan data bersebelahan
lalu ada for i yg mana (n -1), artinya jika jumlah nama yang dimasukan adalah 5 maka jadi 4 yang mana dari 0-4(jadi fungsinya supaya jumlahnya tidak berlebih)
didalam i ada for j (n - i - 1) dimana jika n=5 maka akan dikurang i yang mana tadi jadi 4 dan dikurang 1 jadi mulai dari index 0
nah baru mulai bandingkan yg mana jika arr[j] yg mana tadi 0 dan > arr[j + 1] jadi 0+1 jadi membandingkan array 0 dengan 1 dan juga ada lower yg berfungsi supaya semua nama jadi huruf kecil yang mana ini supaya proses pengurutan tidak terpaku pada kapital
lalu terakhir jika nilai index 0 lebih besar makan akan memulai fungsi tukar

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/1984b9ef4fbae57e2d2dc17b372e111a093ab511/img2/Screenshot%202026-05-01%20153946.png)

    def main():
        try:
            n = int(input("Masukkan jumlah mahasiswa: "))
        except ValueError:
            print("Input tidak valid!")
            return
selanjutnya main koding yg mana memulai program pengurutan nama siswa dimulai dari menentukan jumlah nama yg dimasukkan berupa integer jika bukan int maka akan memcetak ("Input tidak valid!") dan program akan mulai ulang ke masukan jumlah nama 

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/1984b9ef4fbae57e2d2dc17b372e111a093ab511/img2/Screenshot%202026-05-01%20153955.png)

        arr = []
        print("Masukkan nama mahasiswa:")
        for i in range(n):
            nama = input(f"Nama ke-{i+1}: ")
            arr.append(nama)
lanjut ke membuat array kosong untuk memasukkan nama mahasiswa dan cetak "Masukkan nama mahasiswa:", kemudian membuat loop sesuai jumlah nama yang mau dimasukan sebelumnya dan menambahkan nama mahasiswa dengan append yang berfungsi menambahkan variabel di terakhir

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/1984b9ef4fbae57e2d2dc17b372e111a093ab511/img2/Screenshot%202026-05-01%20154005.png)

        print("\nData sebelum diurutkan:")
        for i in range(n):
            print(f"{i+1}. {arr[i]}")
kodingan ini untuk mencetak data sebelum diurutkan

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/1984b9ef4fbae57e2d2dc17b372e111a093ab511/img2/Screenshot%202026-05-01%20154025.png)

        bubble_sort(arr, n)
        print("\nData setelah diurutkan (Bubble Sort):")
        for i in range(n):
            print(f"{i+1}. {arr[i]}")
nah ini setelah diurutkan, dimulai dari pemanggilan fungsi bubble_sort yang mana sudah mulai melakukan sorting data nama mahasiswa, dan melakukan cetak nama setelah diurutkan

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/1984b9ef4fbae57e2d2dc17b372e111a093ab511/img2/Screenshot%202026-05-01%20154037.png)

    if __name__ == "__main__":
        main()
untuk ini fungsinya memulai program main secara keseluruhan

D. Output Program
=================

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/1984b9ef4fbae57e2d2dc17b372e111a093ab511/img2/Screenshot%202026-05-01%20154432.png)
Saat dijalankan dibuka dengan input "Masukkan jumlah mahasiswa: " untuk jumlah tergantung berpa jumlah nama yang mau diurutkan

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/1984b9ef4fbae57e2d2dc17b372e111a093ab511/img2/Screenshot%202026-05-01%20154450.png)
lalu saat sudah menentukan berpa jumlah yang mau diurutkan akan diperintahkan memasukan nama mahasiswa yang mau diurutkan sesuai jumlahnya

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/1984b9ef4fbae57e2d2dc17b372e111a093ab511/img2/Screenshot%202026-05-01%20154718.png)
contoh disini saya sudah memasukkan 10 nama mahasiswa yang mau disorting

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/1984b9ef4fbae57e2d2dc17b372e111a093ab511/img2/Screenshot%202026-05-01%20154737.png)
disini akan dicetak nama- nama mahasiswa yag masih berantakan sebelum dilakukan bubble sort

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/1984b9ef4fbae57e2d2dc17b372e111a093ab511/img2/Screenshot%202026-05-01%20154749.png)
disini saat sudah dilakukan bubble sort, terlihat jelas bahwa nama mahasiswa yang mana tadi berantakanjadi rapi sesuai abjad(A-Z)

e. Link YouTube
===============
Link Video Demo:
(https://youtu.be/P_mE6h-MGxg)

Kesimpulan
==========
Program yang dibuat ini berhasil mengurutkan data nama mahasiswa menggunakan algoritma Bubble Sort dengan baik. Proses pengurutan dilakukan dengan membandingkan elemen yang bersebelahan lalu menukarnya jika tidak sesuai urutan, hingga seluruh data tersusun rapi secara alfabet.

Dari pembuatan program ini, dapat dipahami bahwa Bubble Sort merupakan algoritma yang sederhana dan mudah diimplementasikan, meskipun kurang efisien untuk data dalam jumlah besar. Namun, untuk kasus sederhana seperti pengurutan nama mahasiswa, algoritma ini sudah cukup efektif dan mudah dipahami.
