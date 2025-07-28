# 1. Contoh List (Sebagai Perbandingan)
print("\n--- Contoh List (Akses dengan Indeks) ---")
data_list = ["Ucup", "Otong", "Dudung"]
print(f"List: {data_list}")
print(f"Akses elemen indeks 0: {data_list[0]}") # Output: Ucup

# 2. Membuat dan Mencetak Dictionary Dasar
print("\n--- Membuat Dictionary Dasar (Key:Value) ---")
data_dictionary_sederhana = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value3'
}
print(f"Dictionary sederhana: {data_dictionary_sederhana}")

# 3. Mengakses Elemen Dictionary dengan Key
print("\n--- Mengakses Elemen Dictionary dengan Key ---")
data_teman = {
    'cp': 'Ucup',
    'tg': 'Otong',
    'dg': 'Dudung'
}
print(f"Dictionary teman: {data_teman}")
print(f"Akses dengan key 'cp': {data_teman['cp']}") # Output: Ucup
print(f"Akses dengan key 'tg': {data_teman['tg']}") # Output: Otong

# 4. Dictionary dengan Berbagai Tipe Data untuk Key dan Value
print("\n--- Dictionary dengan Berbagai Tipe Data ---")
data_campuran_dict = {
    'nama_lengkap': 'Ucup Surucup',
    'umur': 25,
    'menikah': False,
    100: 'Seratus', # Key bisa angka
    'hobi': ['membaca', 'coding'], # Value bisa list
    'alamat': { # Value bisa dictionary lain (nested dictionary)
        'jalan': 'Jl. Kembang No. 10',
        'kota': 'Jakarta'
    }
}
print(f"Dictionary campuran: {data_campuran_dict}")
print(f"Akses 'nama_lengkap': {data_campuran_dict['nama_lengkap']}")
print(f"Akses key angka 100: {data_campuran_dict[100]}")
print(f"Akses hobi: {data_campuran_dict['hobi']}")
print(f"Akses kota dari alamat: {data_campuran_dict['alamat']['kota']}")