import os
import CRUD as CRUD

if __name__ == "__main__":
    sistem_operasi = os.name # os.name berfungsi untuk melihat OS apa yang digunakan ketika menjalankan program ini
    
    match sistem_operasi:   # Syntax 'match' untuk menyesuaikan keadaan progam yang akan di jalankan
        case "posix": os.system("clear")
        case "nt": os.system("cls")

    print("SELAMAT DATANG DI PROGRAM")
    print("DATABASE PERPUSTAKAAN")
    print("=========================")

    CRUD.init_console()

    """
    proses di atas akan di proses pertama kali sebelum memasuki ke proses while loop.
    Jadi akan di cek terlebih dahulu untuk databasenya apakah sudah ada atau belum.
    """

    while(True):
        match sistem_operasi:   # Syntax 'match' untuk menyesuaikan keadaan progam yang akan di jalankan
            case "posix": os.system("clear")
            case "nt": os.system("cls")
        
        print("SELAMAT DATANG DI PROGRAM")
        print("DATABASE PERPUSTAKAAN")
        print("=========================")

        print(f"1. Read Data")
        print(f"2. Create Data")
        print(f"3. Update Data")
        print(f"4. Delete Data\n")

        user_option = input("Masukan opsi: ")

        print("\n=========================\n")

        match user_option:
            case "1": CRUD.read_console()
            case "2": CRUD.create_console()
            case "3": CRUD.update_console()
            case "4": print("Delete Data")

        print("\n=========================\n")
        is_done = input("Apakah Selesai (y/n)? ")
        if is_done == "y" or is_done == "Y":
            break

    print("Program Berakhir")

    