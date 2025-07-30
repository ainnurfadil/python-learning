# *args

'''
Digunakan ketika fungsi menerima banyak data input sekaligus dan di tampung hanya 1
Argument saja.
'''

# Basic sturcture
## Bentuk 1
def fungsi(nama,tinggi,berat):  # Urutan Argument sama dengan inputan
    print(f'{nama} tinggi {tinggi}, berat badan {berat}')

fungsi("Ucup",180,60)   # Input dari ini, setiap nilai memiliki Argument sendiri.

## Bentuk 2
def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]          # Nilai ini sesuai dengan nilai data_list yang diberikan oleh fungsi()
    nim = data[1]           # Nilai ini sesuai dengan nilai data_list yang diberikan oleh fungsi()
    semester = data[2]      # Nilai ini sesuai dengan nilai data_list yang diberikan oleh fungsi() 
    print(f'{nama} NIM {nim}, semester {semester}')

fungsi(["Hendro",2502108495,7])


# Penggunaan *args
def fungsi(*args):
    args_data = args
    nama = args_data[0]          
    nim = args_data[1]           
    semester = args_data[2]      
    print(f'{nama} NIM {nim}, semester {semester}')

fungsi("Hendri",2502108495,7)

def fungsi(*args):
    args_data = args
    nama = args_data[0]          
    nim = args_data[1]           
    semester = args_data[4]      
    print(f'{nama} NIM {nim}, semester {semester}')

fungsi("Hendri",2502108495,7,5,6,7,8)

# Studi kasus
def penjumlahan_nilai(*jumlah):
    nilai_awal = 0
    for perulangan in jumlah:
        nilai_awal += perulangan
    return nilai_awal

hasil = penjumlahan_nilai(1,2,3,4,5,6,9,8,7,6)

print(f'hasil penjumlahan dari data = {hasil}')