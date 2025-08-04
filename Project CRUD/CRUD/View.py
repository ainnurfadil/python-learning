# Berisi function untuk memberikan visual dari databasenya

from . import Operasi

def create_console():
    print("\n\n"+"="*100)
    print("Tambah data buku baru")
    penulis = input("Penulis\t: ")
    judul = input("Judul\t: ")
    while(True):
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Tahun tidak lebih dari 4 angka (YYYY)")
        except:
            print("Tahun harus angka")

    Operasi.create(tahun,judul,penulis)

    print('Data sudah masuk')
    read_console()

def read_console():
    data_file = Operasi.read()
    
    index = "No"
    judul = "Judul"
    penulis = "Penulis"
    tahun = "Tahun"

    # Header
    print("\n"+"="*100)
    print(f"{index:4} | {judul:40} | {penulis:40} | {tahun:5}")
    print("-"*100)
    
    # Data
    for index,data in enumerate(data_file):
        data_break = data.split(",")    # Split data dari file bank_data.txt berdasarkan tanda koma
        pk = data_break[0]
        date_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]
        print(f"{index+1:4} | {judul:.40} | {penulis:.40} | {tahun:4}",end="")
        """
        Index dalam print, memulai dari angka 0 jadi ketika mau start di angka 1 ditambahkan 1.

        """
    # Footer
    print("="*100+"\n")

def update_console():
    read_console()
    index_buku = int(input('Pilih nomor buku : '))
    