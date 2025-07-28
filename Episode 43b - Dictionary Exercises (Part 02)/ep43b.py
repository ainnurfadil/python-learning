import datetime
import os 
import string
import random

os.system('cls')  # Untuk Windows

template_data_mahasiswa = {
    'nama':'nama',
    'nim':'0000000000',
    'sks_lulus':0,
    'lahir':datetime.datetime(1111,1,11)
}

data_mahasiswa = {} # Tempat penyimpanan data baru yang di input user
print(f"{'WELCOME':^30}")
print(f"{'NEW COMERS':^30}")
print("="*30)

while True:

    mahasiswa = dict.fromkeys(template_data_mahasiswa.keys())
    mahasiswa['nama'] = input("Nama Mahasiswa: ")
    mahasiswa['nim'] = input("NIM Mahasiswa: ")
    mahasiswa['sks_lulus'] = int(input("SKS Mahasiswa: "))
    TAHUN_LAHIR = int(input("Tahun lahir (YYYY): "))
    BULAN_LAHIR = int(input("Bulan lahir (1-12): "))
    HARI_LAHIR = int(input("Tanggal lahir (1-31): "))
    mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,HARI_LAHIR)
    print(mahasiswa)

    KEY = ''.join((random.choice(string.ascii_uppercase)for i in range(6))) # fungsi ini menggenerate key secara random

    data_mahasiswa.update({KEY:mahasiswa})

    print(f"\n{'KEY':<6} {'NAMA':<17} {'NIM': <10} {'SKS':<3} {'LAHIR':<10}")
    print("="*50)

    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa

        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']
        SKS = data_mahasiswa[KEY]['sks_lulus']
        # BEASISWA = data_mahasiswa[KEY]['beasiswa']
        LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")
        
        print(f"{KEY:<6} {NAMA:<17} {NIM: <10} {SKS:<3} {LAHIR:<10}")

    print('\n')
    is_done = input("Pun mantun (y/n)? ")
    if is_done == "n":
        break
    

print("\nwes beres bro")

