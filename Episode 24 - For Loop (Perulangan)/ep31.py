# Data contoh
data_angka = [1, 5, 2, 3, 4, 6, 4, 3, 2, 3]
data_nama = ["Ucup", "Otong", "Dudung", "Ujang", "Asep", "Gilang"]

print(f"Data Angka Awal: {data_angka}")
print(f"Data Nama Awal: {data_nama}")

# 1. Menghitung Jumlah Kemunculan Data (count())
print("\n--- Menghitung Kemunculan (count()) ---")
jumlah_data_4 = data_angka.count(4)
print(f"Jumlah angka 4 dalam data_angka: {jumlah_data_4}")

jumlah_data_3 = data_angka.count(3)
print(f"Jumlah angka 3 dalam data_angka: {jumlah_data_3}")

jumlah_otong_nama = data_nama.count("Otong")
print(f"Jumlah 'Otong' dalam data_nama: {jumlah_otong_nama}")

# 2. Mengambil Posisi/Indeks Data (index())
print("\n--- Mengambil Posisi/Indeks (index()) ---")
index_dudung = data_nama.index("Dudung")
print(f"Index dari 'Dudung': {index_dudung}")

index_pertama_3 = data_angka.index(3)
print(f"Index pertama dari angka 3: {index_pertama_3}")

# Jika elemen tidak ada, akan terjadi ValueError
# try:
#     index_non_existent = data_nama.index("Budi")
#     print(f"Index 'Budi': {index_non_existent}")
# except ValueError as e:
#     print(f"Error: {e} - 'Budi' tidak ada dalam list.")

# 3. Mengurutkan List (sort())
print("\n--- Mengurutkan List (sort()) ---")
print(f"Data Angka sebelum sort: {data_angka}")
data_angka.sort() # Mengurutkan secara in-place
print(f"Data Angka setelah sort: {data_angka}")

print(f"Data Nama sebelum sort: {data_nama}")
data_nama.sort() # Mengurutkan secara in-place (alfabetis)
print(f"Data Nama setelah sort: {data_nama}")

# 4. Membalik Urutan List (reverse())
print("\n--- Membalik Urutan (reverse()) ---")
print(f"Data Angka sebelum reverse: {data_angka}")
data_angka.reverse() # Membalik urutan secara in-place
print(f"Data Angka setelah reverse: {data_angka}")

print(f"Data Nama sebelum reverse: {data_nama}")
data_nama.reverse() # Membalik urutan secara in-place
print(f"Data Nama setelah reverse: {data_nama}")