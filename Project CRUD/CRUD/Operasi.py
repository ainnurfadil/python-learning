# File ini untuk menjalankan operasi untuk menulis database

from time import time
from . import Database
from .Util import random_string
import time

def update(no_buku,pk,data_add,judul,penulis,tahun):
    data = Database.TEMPLATE.copy()

    data["pk"] = pk
    data["date_add"] = data_add
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'
    
    panjang_data = len(data_str)

    try:
        with(open(Database.DB_NAME,'r+',encoding="utf-8")) as file:
            file.seek(panjang_data*(no_buku-1))
            file.write(data_str)
    except:
        print("error dalam update data")

def create(tahun,judul,penulis):
    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = tahun

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'

    try:
        with open(Database.DB_NAME,'a',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Gagal memasukkan data")    


def create_first_data():
    penulis = input("Penulis: ")
    judul = input("Judul: ")
    while(True):
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Tahun tidak lebih dari 4 angka (YYYY)")
        except:
            print("Tahun harus angka")

    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    """
    untuk time.strftime(), nilainya perwakilan awal hurus keterangan, untuk yang kecil mewakili nama kalender,
    untuk yang besar mewakili satuan waktu jam kecuali %Y ada century year nya (nominal ribuan). 
    %z disini memiliki arti offset dari satuan waktu UTC.
    """
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = tahun

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'
    print(data_str)
    try:
        with open(Database.DB_NAME,'w',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Gagal memasukkan data")

def read(**kwargs):
    try:
        with open(Database.DB_NAME, 'r') as file:
            content = file.readlines()          # Membaca semua data dalam file bank_data.txt menjadi data List
            jumlah_buku = len(content)          # Mengetahui jumlah buku berdasarkan list yang ada di bank_data.txt
            if "index" in kwargs:               # Setelah mendapatkan nilai inputan dari kwargs, kemudian mencocokkan nilai dengan nomor index yang di input dari update_console
                index_buku = kwargs["index"]-1
                if index_buku < 0 or index_buku > jumlah_buku:
                    return False
                else:
                    return content[index_buku] 
            else:
                return content
    except:
        print("Membaca database error")
        return False