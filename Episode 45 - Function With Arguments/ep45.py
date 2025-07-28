# Fungsi dengan argument (input)

'''
Template dari fungsi:
def nama_fungsi(argument)
    badan fungsi

Jadi yang di dalam kurung itu adalah tempat untuk memberikan nilai inputan yang
bisa di eksekusi dalam badan fungsi. Sebutannya bisa input, argument atau parameter.
'''

def hello_world(nama):
    ## fungsi hello_world menerima input dengan variable nama
    print(f"Selamat datang dunia wahai {nama}")

hello_world("Udin")

# Program menambah 

def tambah(angka_01,angka_02):
    hasil = angka_01 + angka_02
    print(f"{angka_01} + {angka_02} = {hasil}")

tambah(2,5)
tambah(500,999)

# Program fungsi looping

def looping_nama(c):    # Dalam hal ini, argument c dan anggota_parpol nilainya sama
    a = c.copy()
    for b in a:
        print(f"\nYang muliyono {b}")

anggota_parpol = ["prabowo","jokowi","fufufafa"]

looping_nama(anggota_parpol)

## Kita bisa memanipulasi list yang ada di luar fungsi melalui

def looping_nama(c):    # Dalam hal ini, argument c dan anggota_parpol nilainya sama
    a = c.copy()
    for b in a:
        print(f"\nYang muliyono {b}")

anggota_parpol = ["prabowo","jokowi","fufufafa"]

looping_nama(anggota_parpol)
