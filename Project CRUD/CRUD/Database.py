# file ini untuk mendeteksi apakah sudah ada file data base atau belum

from . import Operasi

DB_NAME = "bank_data.txt"                # file dari data basenya
TEMPLATE = {                        # Membuat standart template untuk isi data
    "pk":"XXXXXX",                  # "pk" disini artinya Primary Key
    "date_add":"yyyy-mm-dd",
    "judul":255*" ",
    "penulis":255*" ",
    "tahun":"yyyy"
}

def init_console():         # Function untuk cek apakah sudah ada data base, kalau belum ada akan ada proses membuat data base baru
    try:
        with open(DB_NAME,"r") as file:
            print("Database tersedia, init done!")
    except:
        print("Database tidak ditemukan, silahkan membuat database baru")
        Operasi.create_first_data()

