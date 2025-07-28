# 1. Contoh Dasar 'break'
print("\n--- Contoh Dasar 'break' ---")
angka = 0
while angka < 5:
    angka += 1
    print(f"Angka sekarang: {angka}")
    if angka == 3:
        print("Mendeteksi angka 3, akan break...")
        break # Menghentikan loop sepenuhnya
    print("Ini akan dieksekusi jika break tidak terpanggil.")
print("Cukup finish.")

# 2. Contoh 'break' dengan Input Pengguna
print("\n--- Contoh 'break' dengan Input Pengguna ---")
angka_input = 0
print("Program akan menghitung sampai batas yang Anda masukkan.")
while True: # Loop yang berpotensi tak terbatas
    angka_input += 1
    print(f"Hitungan ke: {angka_input}")
    
    try:
        batas = int(input("Masukkan batas hitungan (masukkan 0 untuk keluar): "))
        if batas == 0:
            print("Anda memilih untuk keluar.")
            break
        elif angka_input >= batas: # Jika hitungan sudah mencapai atau melebihi batas
            print(f"Hitungan mencapai batas {batas}, break...")
            break
    except ValueError:
        print("Input tidak valid, masukkan angka.")
        continue # Lanjut ke iterasi berikutnya jika input salah
