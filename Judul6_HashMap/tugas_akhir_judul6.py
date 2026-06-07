class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMapSeparateChaining:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [None] * self.SIZE

    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE

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
            break
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()