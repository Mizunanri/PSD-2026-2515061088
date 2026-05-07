def sequential_search(data, n, target):
    i = 0
    while i < n:
        if data[i].lower() == target.lower():
            return i
        i += 1
    return -1


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

    print("=== Sistem Pencarian Data Pasien ===")
    print(f"Data pasien : {data}")
    target = input("Masukkan nama pasien yang dicari: ")
    posisi = sequential_search(data, n, target)

    if posisi != -1:

        print("\nData pasien ditemukan")
        print(f"Nama pasien        : {data[posisi]}")
        print(f"Tempat rawat inap  : {ruangan[posisi]}")
        print(f"Status pasien      : {status[posisi]}")

    else:
        print("\nData pasien tidak ditemukan")


if __name__ == "__main__":
    main()