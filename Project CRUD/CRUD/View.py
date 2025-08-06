# Berisi function untuk memberikan visual dari databasenya

from . import Operasi

def delete_console():
    read_console()
    while(True):
        print("Silahkan pilih nomor buku yang akan di delete")
        no_buku = int(input("Nomor Buku: "))
        data_buku = Operasi.read(index=no_buku)

        if data_buku:
            data_break = data_buku.split(',')
            pk = data_break[0]
            data_add = data_break[1]
            penulis = data_break[2]
            judul = data_break[3]
            tahun = data_break[4][:-1]

    
            # data yang ingin diupdate
            print("\n"+"="*100)
            print("Data yang ingin anda Hapus")
            print(f"1. Judul\t: {judul:.40}")
            print(f"2. Penulis\t: {penulis:.40}")
            print(f"3. Tahun\t: {tahun:4}")
            is_done = input("Apakah anda yakin (y/n)? ")
            if is_done == "y" or is_done == "Y":
                Operasi.delete(no_buku)
                break
        else:
            print("nomor tidak valid, silahkan masukan lagi")

    print("Data berhasil di hapus")

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
    while(True):
        print("Pilih nomor buku yang tertera di tampilan untuk di update")
        no_buku = int(input('Pilih nomor buku : '))
        data_buku = Operasi.read(index=no_buku)

        if data_buku:
            break
        else:
            print("Nomor tidak valid")

    data_break = data_buku.split(',')
    pk = data_break[0]
    data_add = data_break[1]
    judul = data_break[3]
    penulis = data_break[2]
    tahun = data_break[4][:-1]

    while (True):
        print("\n"+"="*100)
        print("silahkan pilih data apa yang ingin diubah")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")

        user_option = input("Pilih yang akan di edit [1,2,3]: ")
        print("\n"+"="*100)
        match user_option:
            case "1": judul = input("Judul\t: ")
            case "2": penulis = input("Penulis\t: ")
            case "3":     
                while(True):
                    try:
                        tahun = int(input("Tahun\t: "))
                        if len(str(tahun)) == 4:
                            break
                        else:
                            print("Tahun tidak lebih dari 4 angka (YYYY)")
                    except:
                        print("Tahun harus angka")
            case _: print("Index tidak ada.")

        print("Data Baru")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")
        is_done = input("Apakah sudah cocok (y/n)? ")
        if is_done == "y" or is_done == "Y":
            break
    
    Operasi.update(no_buku,pk,data_add,judul,penulis,tahun)

