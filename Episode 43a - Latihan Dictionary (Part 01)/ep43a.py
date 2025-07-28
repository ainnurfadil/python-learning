# Latihan Dictionary

# Membuat dictionary berdasarkan inputan User

import datetime
import os 

os.system('cls')  # Untuk Windows

template_data_mahasiswa = {
    'nama':'nama',
    'nim':'0000000000',
    'sks_lulus':0,
    'lahir':datetime.datetime(1111,1,11)
}

data_mahasiswa = {} # Data kosong

print(f"{'WELCOME':^30}")
print(f"{'NEW COMERS':^30}")
print("="*30)

mahasiswa = dict.fromkeys(template_data_mahasiswa.keys())
print(mahasiswa)
mahasiswa['nama'] = input("Nama Mahasiswa: ")
mahasiswa['nim'] = input("NIM Mahasiswa: ")
mahasiswa['sks_lulus'] = int(input("SKS Mahasiswa: "))
TAHUN_LAHIR = int(input("Tahun lahir (YYYY): "))
BULAN_LAHIR = int(input("Bulan lahir (1-12): "))
HARI_LAHIR = int(input("Tanggal lahir (1-31): "))
mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,HARI_LAHIR)
print(mahasiswa)