# 1. Membuat Nested List Dasar
print("\n--- Nested List Dasar ---")
data_nol = [1, 2]
data_satu = [3, 4]

list_2d = [data_nol, data_satu]
print(f"list_2d = {list_2d}") # Output: [[1, 2], [3, 4]]

list_campuran = [data_nol, data_satu, 5, "enam"]
print(f"list_campuran = {list_campuran}") # Output: [[1, 2], [3, 4], 5, 'enam']

# 2. Contoh Penggunaan Nested List (Data Peserta)
print("\n--- Contoh Data Peserta ---")
peserta_0 = ["Ucup", 25, "laki-laki"]
peserta_1 = ["Otong", 10, "laki-laki"]
peserta_2 = ["Dedeh", 50, "wanita"]

list_peserta = [peserta_0, peserta_1, peserta_2]
print(f"list_peserta = {list_peserta}")

# Menampilkan data peserta dengan looping
print("\n--- Menampilkan Detail Peserta ---")
for i, peserta in enumerate(list_peserta):
    print(f"Peserta ke-{i+1}:")
    print(f"  Nama\t: {peserta[0]}")
    print(f"  Umur\t: {peserta[1]}")
    print(f"  Gender: {peserta[2]}\n")

# 3. Permasalahan Shallow Copy pada Nested List
print("\n--- Permasalahan Shallow Copy (Nested List) ---")
list_copy = list_peserta.copy()
print(f"list_peserta (asli) = {list_peserta}")
print(f"list_copy (shallow copy) = {list_copy}")

# Mengubah elemen di dalam sub-list pada list asli
list_peserta[0][0] = "Michael"
list_peserta[0][1] = 99

print(f"\nSetelah list_peserta[0][0] diubah jadi 'Michael' dan [0][1] jadi 99:")
print(f"list_peserta (setelah diubah) = {list_peserta}")
print(f"list_copy (juga ikut berubah)  = {list_copy}") # Ini menunjukkan masalah shallow copy
