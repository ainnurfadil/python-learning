data_dictionary = {
    "Cup": "Ucup Surucup",
    "Tong": "Otong Surotong",
    "Dung": "Dudung Surudung"
}
print(f"Dictionary awal: {data_dictionary}")

# 1. Mengambil Panjang Dictionary (len())
print("\n--- Mengambil Panjang Dictionary (len()) ---")
panjang_dict = len(data_dictionary)
print(f"Panjang dictionary adalah: {panjang_dict}")

# 2. Mengecek Keberadaan Key ('in' operator)
print("\n--- Mengecek Keberadaan Key ('in') ---")
key_to_check_1 = "Cup"
is_key_exist_1 = key_to_check_1 in data_dictionary
print(f"Apakah key '{key_to_check_1}' ada di dictionary: {is_key_exist_1}")

key_to_check_2 = "Kis"
is_key_exist_2 = key_to_check_2 in data_dictionary
print(f"Apakah key '{key_to_check_2}' ada di dictionary: {is_key_exist_2}")

# 3. Mengakses Value (dengan [] atau .get())
print("\n--- Mengakses Value ---")
# Cara biasa (akan error jika key tidak ada)
print(f"Akses 'Tong' dengan []: {data_dictionary['Tong']}")

# Menggunakan .get() (lebih aman)
print(f"Akses 'Cup' dengan .get(): {data_dictionary.get('Cup')}")
print(f"Akses 'Kis' dengan .get() (key tidak ada): {data_dictionary.get('Kis')}") # Output: None
print(f"Akses 'Kis' dengan .get() dan default value: {data_dictionary.get('Kis', 'Key tidak ditemukan!')}")

# 4. Mengupdate Data (mengubah/menambah)
print("\n--- Mengupdate Data ---")
# Mengubah value yang sudah ada
data_dictionary["Cup"] = "Ucup si Ganteng"
print(f"Setelah 'Cup' diubah: {data_dictionary}")

# Menambah pasangan key-value baru (jika key belum ada)
data_dictionary["Sep"] = "Asep si Kasep"
print(f"Setelah menambah 'Sep': {data_dictionary}")

# Menggunakan .update()
# Memperbarui existing key
data_dictionary.update({"Tong": "Otong si Jagoan"})
print(f"Setelah update 'Tong': {data_dictionary}")

# Menambah key baru dengan .update()
data_dictionary.update({"Faqih": "Faqih si Paling Keren"})
print(f"Setelah update/tambah 'Faqih': {data_dictionary}")

# 5. Menghapus Data (del)
print("\n--- Menghapus Data (del) ---")
del data_dictionary["Faqih"]
print(f"Setelah menghapus 'Faqih': {data_dictionary}")