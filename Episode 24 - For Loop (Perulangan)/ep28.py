# 1. Segitiga Siku-siku Menggunakan 'for'
print("\n--- Segitiga Siku-siku (for) ---")
sisi_for = 5
count_for = 1
for i in range(sisi_for):
    print("*" * count_for)
    count_for += 1
print("Akhir dari segitiga for.")

# 2. Segitiga Siku-siku Menggunakan 'while'
print("\n--- Segitiga Siku-siku (while) ---")
sisi_while = 5
count_while = 1
while True:
    print("*" * count_while)
    count_while += 1
    if count_while > sisi_while:
        break
print("Akhir dari segitiga while.")

# 3. Segitiga dengan Baris Ganjil Saja (while dan continue)
print("\n--- Segitiga Baris Ganjil ---")
sisi_ganjil = 7
count_ganjil = 0
while True:
    count_ganjil += 1 # Pastikan ini selalu bertambah
    if count_ganjil % 2 == 0: # Jika genap, skip
        continue

    print("*" * count_ganjil) # Akan print jika ganjil

    if count_ganjil >= sisi_ganjil: # Perbaikan kondisi break
        break
print("Akhir dari segitiga ganjil.")

# 4. Segitiga Sama Kaki (Mengembangkan dari nomor 3)
print("\n--- Segitiga Sama Kaki ---")
sisi_sama_kaki = 9 # Disarankan angka ganjil untuk simetris
count_sama_kaki = 0
spasi_awal = sisi_sama_kaki // 2 # Menggunakan integer division untuk spasi awal

while True:
    count_sama_kaki += 1

    if count_sama_kaki % 2 == 0: # Jika genap, skip
        continue

    # Cetak spasi diikuti bintang/plus
    print(" " * spasi_awal + "+" * count_sama_kaki)
    spasi_awal -= 1 # Kurangi spasi untuk baris ganjil berikutnya

    if count_sama_kaki >= sisi_sama_kaki: # Kondisi break
        break