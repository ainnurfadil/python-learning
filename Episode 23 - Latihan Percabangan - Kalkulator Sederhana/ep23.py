print("="*25)

# Input Angka
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

# Input Operator
operator = input("Masukkan operator (+,-,*,/): ")

# Logika Percabangan (if-elif-else)
if operator == "+":
    hasil = angka1 + angka2
    print(f"Hasilnya adalah: {hasil}")
elif operator == "-":
    hasil = angka1 - angka2
    print(f"Hasilnya adalah: {hasil}")
elif operator == "*" or operator == "x": # Menangani dua kemungkinan input untuk perkalian
    hasil = angka1 * angka2
    print(f"Hasilnya adalah: {hasil}")
elif operator == "/":
    hasil = angka1 / angka2
    print(f"Hasilnya adalah: {hasil}")
else:
    print("Masukkan operator yang benar dong!") # Pesan error jika operator salah

print("="*25)