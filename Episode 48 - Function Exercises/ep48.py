# Contoh fungsi program menghtung luas dan kelili
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

    print(f'\nHasil dari luas = {luas}')
    print(f'Hasil dari keliling = {keliling}')

    isContinue = input("\nApakah mau lanjut (y/n)? ")

    if isContinue == "n" or "N":
        break
    
print(f"{"="*40:^40}")
print(f"{"PROGRAM SELESAI":^40}")