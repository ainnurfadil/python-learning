# 1. Contoh Manual Tanpa Loop (Ilustrasi Kebutuhan Loop)
print("\n--- Contoh Manual (Tanpa Loop) ---")
angka = 1
print(angka)
angka = angka + 1
print(angka)
angka = angka + 1
print(angka)

# 2. Looping dengan List
print("\n--- Looping dengan List ---")
angka_angka_list = [10, 20, 30, 40, 50]
for i in angka_angka_list:
    print(f"i sekarang -> {i}")
print("akhir dari program 1")

# 3. Looping dengan range() (Dasar)
print("\n--- Looping dengan range() ---")
for i in range(5): # range(5) menghasilkan 0, 1, 2, 3, 4
    print(f"i sekarang -> {i}")
print("akhir dari program 2")

# 4. Looping dengan range() (Dengan Batas Awal dan Akhir)
print("\n--- Looping dengan range(start, stop) ---")
for i in range(1, 5): # range(1, 5) menghasilkan 1, 2, 3, 4
    print(f"i sekarang -> {i}")

print("\n--- Looping dengan range(1, 10) ---")
for i in range(1, 10): # range(1, 10) menghasilkan 1, 2, ..., 9
    print(f"i sekarang -> {i}")

# 5. Looping dengan String
print("\n--- Looping dengan String ---")
data_str = "Saya ganteng abis"
for huruf in data_str:
    print(huruf)