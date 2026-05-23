Sistem Data Nilai Siswa Menggunakan Binary Search Tree (BST)
=======================================================

A. Judul Program
================
Sistem Data Nilai Siswa Menggunakan Binary Search Tree (BST)

B. Deskripsi Singkat
====================

Program ini dibuat untuk mengelola data nilai siswa menggunakan struktur data Binary Search Tree (BST). BST digunakan karena mampu menyimpan data secara terurut dan mempercepat proses pencarian data dibandingkan pencarian biasa.

Pada program ini pengguna dapat menambahkan nilai siswa, mencari nilai tertentu, menampilkan data secara terurut, melihat nilai tertinggi dan terendah, menghitung jumlah data siswa, serta menghitung total seluruh nilai siswa. Program ini menerapkan konsep BST dasar seperti insert, search, inorder traversal, find minimum, find maximum, count nodes, dan sum nodes.


C. Penjelasan Kode
==================

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/ab321d9c5ea88bd78c8e37e0c39e52013438b5bc/img5/Screenshot%202026-05-21%20185427.png)

    class Node:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None
pertama membuat objek/class node tree dengan fungsi dengan parameter self dan key
self berfungsi memanggildiri sendiri lalu untuk left dan right none karena root, nilai kiri dan kanan masih kosong

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/ab321d9c5ea88bd78c8e37e0c39e52013438b5bc/img5/Screenshot%202026-05-21%20185437.png)

    class BSTNilaiSiswa:
        def __init__(self):
            self.root = None

        def insert_node(self, root, key):
            if root is None:
                return Node(key)
            if key < root.key:
                root.left = self.insert_node(root.left, key)
            elif key > root.key:
                root.right = self.insert_node(root.right, key)
            return root
        def insert(self, key):
            self.root = self.insert_node(self.root, key)
selanjutnya memulai dengan memanggil root karena masih kosong lalku ada fungsi insert yang mana ada kondisi jika root ksong maka mengembalikan nilai ke root yg kosong, jika nilai lebih kecil dari nilai root maka melakukan rekursi pada root sebelah kiri yang mana berfungsi memastikan nilai ditempatkan ditempat yang benar dan elif yang sama akan tetapi jika lebih besar maka akan ditempatkan disebelah kanan dan dibawahnya ada fungsi yg akan dijalankan saat memulai insert maka root akan berpindah untuk menempatkan nilai ke tempat yang sesuai  jika sudah nilai dan root akan otomatis menyesuaikan tempat tanpa mengganggu nilai lain.

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/ab321d9c5ea88bd78c8e37e0c39e52013438b5bc/img5/Screenshot%202026-05-21%20185446.png)

        def search_node(self, root, key):
            if root is None:
                return False
            if root.key == key:
                return True
            if key < root.key:
                return self.search_node(root.left, key)
            return self.search_node(root.right, key)
        def search(self, key):
            return self.search_node(self.root, key)

kemudian fungsi search ada 3 parameter yaitu self root dan key(nilai) sebenarnya sama seperti insert akan tetapi hanya untuk mencari nilai saja

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/ab321d9c5ea88bd78c8e37e0c39e52013438b5bc/img5/Screenshot%202026-05-21%20185500.png)

        def inorder(self, root):
            if root is None:
                return
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)
lanjut ke inorder dengan parameter self dan root karena penelusuran dari kiri root lalu kanan ini berfungsi untuk penyusunan nilai yang sudah diinputkan 

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/ab321d9c5ea88bd78c8e37e0c39e52013438b5bc/img5/Screenshot%202026-05-21%20185513.png)

        def find_min(self, root):
            if root is None:
                return -1
            current = root
            while current.left is not None:
                current = current.left
            return current.key

        def find_max(self, root):
            if root is None:
                return -1
            current = root
            while current.right is not None:
                current = current.right
            return current.key
nah masuk ke fungsi find_min untuk mencari nilai min yang mana ada di root bagian kiri konsepnya seperti root sebelah kiri tidak kosong maka current akan dimasukan nilai yang sebelah kiri ini akan terus mencari nilai terkecil sampai selesai. kenapa -1 karna nilainya bukan negatif ataupun root yang kosong.

begitupun juga find_max yang mana mencari nilai terbesar yang mana berada di root bagian kanan.

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/ab321d9c5ea88bd78c8e37e0c39e52013438b5bc/img5/Screenshot%202026-05-21%20185525.png)

    def count_nodes(self, root):
        if root is None:
            return 0
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)

    def sum_nodes(self, root):
        if root is None:
            return 0
        return root.key + self.sum_nodes(root.left) + self.sum_nodes(root.right)
kemudian ada fungsi count_nodes yang mana mengitung total dalam BST dimulai dari cek apakai root kosong jika tidak maka root+total seluruh bagian kiri+total seluruh bagian kanan

dan terakhir sum_nodes yang mana menjumlahkan nilai daris semua nodes sama seperti count_nodesakan tetapi bukan menghitung jumlah tetapi nilai dari seluruh nodes dari root+total seluruh bagian kiri+total seluruh bagian kanan

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/ab321d9c5ea88bd78c8e37e0c39e52013438b5bc/img5/Screenshot%202026-05-21%20185539.png)

    def main():
        bst = BSTNilaiSiswa()
        pilih = 0
        while pilih != 8:
            print("\n=== DATA NILAI SISWA ===")
            print("1. Tambah Nilai")
            print("2. Cari Nilai")
            print("3. Tampilkan Nilai Urut")
            print("4. Nilai Terendah")
            print("5. Nilai Tertinggi")
            print("6. Jumlah Siswa")
            print("7. Total Nilai")
            print("8. Keluar")
            try:
                pilih = int(input("Pilih menu: "))
            except ValueError:
                print("Input tidak valid!")
                continue
lanjut ke fungsi utama sistem dimulai dengan memuat bst dengan memanggil keseluruhan isi BSTNilaiSiswa() lalu pilih dimulai dari 1-8 kalau lebih/kurang pada saat menginput pilih menu maka akan idak valid dan balik lagi ke input pilih menu            

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/ab321d9c5ea88bd78c8e37e0c39e52013438b5bc/img5/Screenshot%202026-05-21%20185642.png)

            if pilih == 1:
                try:
                    nilai = int(input("Masukkan nilai siswa: "))

                    bst.insert(nilai)
                    print(f"Nilai {nilai} berhasil ditambahkan")
                except ValueError:
                    print("Input tidak valid!")
            elif pilih == 2:
                try:
                    nilai = int(input("Cari nilai: "))
                    if bst.search(nilai):
                        print("Nilai ditemukan")
                    else:
                        print("Nilai tidak ditemukan")
                except ValueError:
                    print("Input tidak valid!")
            elif pilih == 3:
                print("Data nilai terurut: ", end="")
                bst.inorder(bst.root)
                print()
            elif pilih == 4:
                print(f"Nilai terendah: {bst.find_min(bst.root)}")
            elif pilih == 5:
                print(f"Nilai tertinggi: {bst.find_max(bst.root)}")
            elif pilih == 6:
                print(f"Jumlah siswa: {bst.count_nodes(bst.root)}")
            elif pilih == 7:
                print(f"Total seluruh nilai: {bst.sum_nodes(bst.root)}")
            elif pilih == 8:
                print("Program selesai")
            else:
                print("Pilihan tidak valid!")
ini adalah opsi dari 8 pilihan tadi 

            if pilih == 1:
                try:
                    nilai = int(input("Masukkan nilai siswa: "))

                    bst.insert(nilai)
                    print(f"Nilai {nilai} berhasil ditambahkan")
                except ValueError:
                    print("Input tidak valid!")

dimulai dari memasukan nilai yang mau dimasukan lalu nilai akan masuk ke fungsi  bst insert kemudian akan dilakukan print jika berhasil kalau yang diinpukan bukan niai maka akan muncul input tidak valid

            elif pilih == 2:
                try:
                    nilai = int(input("Cari nilai: "))
                    if bst.search(nilai):
                        print("Nilai ditemukan")
                    else:
                        print("Nilai tidak ditemukan")
                except ValueError:
                    print("Input tidak valid!")
lanjut ke opsi 2 yaitu mencari nilai sama seperti insert tapi ini mencari nilai jika ketemu maka nilai ditemukan jika tidak maka tidak ditemukan dan jika yang diinput bukan tipe yang sama maka input tidak valid

            elif pilih == 3:
                print("Data nilai terurut: ", end="")
                bst.inorder(bst.root)
                print()
ada juga 3 yang mana mengurutan nilai lalu diakhiri dengan space

            elif pilih == 4:
                print(f"Nilai terendah: {bst.find_min(bst.root)}")
            elif pilih == 5:
                print(f"Nilai tertinggi: {bst.find_max(bst.root)}")
            elif pilih == 6:
                print(f"Jumlah siswa: {bst.count_nodes(bst.root)}")
            elif pilih == 7:
                print(f"Total seluruh nilai: {bst.sum_nodes(bst.root)}")
            elif pilih == 8:
                print("Program selesai")
            else:
                print("Pilihan tidak valid!")
dan masih ada 4-5 dengan mencetak hasil dari fungsinya masing2 dan ada 8 untuk menghentikan sistem dan jika menginput pilihan selain 1-8 maka "Pilihan tidak valid!"

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/ab321d9c5ea88bd78c8e37e0c39e52013438b5bc/img5/Screenshot%202026-05-21%20185651.png)

    if __name__ == "__main__":
        main()
nah terakhir ada untuk memulai program dari awal hingga akhir

D. Output Program
=================

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/ab321d9c5ea88bd78c8e37e0c39e52013438b5bc/img5/Screenshot%202026-05-21%20185942.png)

Sistem dibuka dengan memilih dari 8 pilihan menu

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/ab321d9c5ea88bd78c8e37e0c39e52013438b5bc/img5/Screenshot%202026-05-21%20190000.png)

jika memasukan angka selain 1-8 maka muncul "Pilihan tidak valid!"

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/ab321d9c5ea88bd78c8e37e0c39e52013438b5bc/img5/Screenshot%202026-05-21%20190112.png)

misal disini memilih menu 1 maka akan memasukkan nilai, disini kita sudah memasukan bbrp nilai sebagai contoh

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/ab321d9c5ea88bd78c8e37e0c39e52013438b5bc/img5/Screenshot%202026-05-21%20190134.png)

jika kita mencari(opsi 2) kita akan disuruh input  nilai yang hendak dicari misal disini 70 maka nilai akan ditemukan

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/ab321d9c5ea88bd78c8e37e0c39e52013438b5bc/img5/Screenshot%202026-05-21%20190156.png)

kalau mau melihat urutan data maka pilih opsi 3 maka secara otomatis data akan terurut

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/ab321d9c5ea88bd78c8e37e0c39e52013438b5bc/img5/Screenshot%202026-05-21%20190219.png)

lalu ada opsi 4. Nilai Terendah dan 5. Nilai Tertinggi jika mau melihat dari urutan nilai mana nilai terendah dan tertinggi

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/ab321d9c5ea88bd78c8e37e0c39e52013438b5bc/img5/Screenshot%202026-05-21%20190236.png)

opsi 6 jika kamu mau melihat berapa jumlah ada berapa nilai siswa yang sudah dimasukkan

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/ab321d9c5ea88bd78c8e37e0c39e52013438b5bc/img5/Screenshot%202026-05-21%20190253.png)

opsi 7 jika ingin menjumlahkan keseluruhan nilai siswa yang sudah dimasukkan

![image alt](https://github.com/Mizunanri/PSD-2026-2515061088/blob/ab321d9c5ea88bd78c8e37e0c39e52013438b5bc/img5/Screenshot%202026-05-21%20190314.png)

terakhir opsi 8 untuk mengakhiri program/sistem

e. Link YouTube
===============
Link Video Demo:
(https://youtu.be/FuwCm_3kedU)

Kesimpulan
==========

Program Sistem Data Nilai Siswa Menggunakan Binary Search Tree berhasil dibuat dan dijalankan dengan baik. Program mampu menyimpan data nilai siswa secara terstruktur dan terurut sehingga proses pencarian dan pengolahan data menjadi lebih mudah.

Dari program ini dapat dipahami bahwa Binary Search Tree sangat efektif digunakan untuk pengelolaan data yang membutuhkan proses pencarian dan pengurutan secara cepat.

