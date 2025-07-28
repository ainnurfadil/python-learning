# 1. Contoh Penggunaan 'pass'
print("\n--- Contoh 'pass' ---")
angka = 0
while angka < 5:
    angka += 1
    if angka == 3:
        pass # Tidak melakukan apa-apa, hanya placeholder
    print(angka)
print("Finish pass example.")

# 2. Contoh Penggunaan 'continue'
print("\n--- Contoh 'continue' ---")
angka = 0
print(f"Angka sekarang (sebelum loop): {angka}")
while angka < 5:
    angka += 1
    print(f"Angka di awal iterasi: {angka}") # Aksi 1
    if angka == 3:
        print("Mendeteksi angka 3, akan continue...") # Aksi dalam kondisi if
        continue      # Melompat ke iterasi berikutnya, melewati kode di bawahnya
    print(f"Ini akan dieksekusi jika angka BUKAN 3. Angka saat ini: {angka}") # Aksi 2
print("Finish continue example.")