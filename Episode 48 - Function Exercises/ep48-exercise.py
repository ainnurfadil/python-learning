# Menambahkan Fungsi input user yang bisa memilih output untuk menghitung Luas atau Keliling
import os

def header():
    os.system("cls")
    print(f"{'PROGRAM MENGHIUNG':^40}")
    print(f"{'LUAS DAN KELILING':^40}")
    print(f"{"="*40:^40}")

def input_user():
    panjang = float(input("Masukkan nilai Panjang : "))
    lebar = float(input("Masukkan nilai Panjang : "))
    return panjang,lebar

def hitung_luas(panjang,lebar):
    hasil = panjang*lebar
    return hasil

def hitung_keliling(panjang,lebar):
    hasil = 2*(panjang*lebar)
    return hasil

while True:
    header()
    lebar,panjang = input_user()
    luas = hitung_luas(panjang,lebar)
    keliling = hitung_keliling(panjang,lebar)

    print(f"Mau menghitung yang mana?")
    print(f"1. Luas")
    print(f"2. Keliling")
    pilihan = int(input(f"Masukkan angka = "))

    if pilihan == 1:
        print(f'\nHasil dari luas = {luas}')
    elif pilihan == 2:
        print(f'Hasil dari keliling = {keliling}')

    isContinue = input("\nApakah mau lanjut (y/n)? ")

    if isContinue == "n":
        break
    
print(f"{"="*40:^40}")
print(f"{"PROGRAM SELESAI":^40}")