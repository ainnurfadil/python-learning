kumpulan_angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
peserta_nama = ["Ucup", "Otong", "Dadang", "Diding", "Duduk"]

# 1. Looping dengan 'for' loop sederhana (Mengambil Elemen)
print("\n--- Looping 'for' (elemen) ---")
for angka in kumpulan_angka:
    print(f"Angka = {angka}")

for nama in peserta_nama:
    print(f"Nama = {nama}")

# 2. Looping dengan 'for' loop dan range() (Mengambil Indeks dan Elemen)
print("\n--- Looping 'for' dengan range() (indeks) ---")
panjang_angka = len(kumpulan_angka)
for i in range(panjang_angka):
    print(f"Indeks = {i}, Angka = {kumpulan_angka[i]}")

# 3. Looping dengan 'while' loop
print("\n--- Looping 'while' ---")
i_while = 0
panjang_peserta = len(peserta_nama)
while i_while < panjang_peserta:
    print(f"Indeks = {i_while}, Nama = {peserta_nama[i_while]}")
    i_while += 1

# 4. Looping dengan List Comprehension (untuk membuat/mengolah)
print("\n--- Looping dengan List Comprehension ---")
# Contoh untuk mencetak (kurang umum, tapi bisa)
print("\n(List Comprehension untuk print - biasanya untuk membuat list baru)")
data_campuran = ["Apel", 123, "Jeruk", True]
[print(f"Data item: {item}") for item in data_campuran]

# Contoh List Comprehension untuk membuat list baru
kuadrat_angka = [i**2 for i in kumpulan_angka]
print(f"\nKuadrat angka: {kuadrat_angka}")

# 5. Looping dengan enumerate() (Mengambil Indeks dan Elemen secara bersamaan)
print("\n--- Looping dengan enumerate() ---")
for indeks, item_data in enumerate(peserta_nama):
    print(f"Indeks = {indeks}, Data = {item_data}")

# Contoh lain dengan enumerate
for idx, num in enumerate(kumpulan_angka):
    if num % 2 == 0:
        print(f"Angka genap di indeks {idx}: {num}")