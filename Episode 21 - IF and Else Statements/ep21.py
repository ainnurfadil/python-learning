# Input nama dari user
nama = input("Siapa nama anda? ")

# 1. Program If Inline (Satu Baris)
print("\n--- If Inline ---")
if nama == "Ucup": print("Kamu ganteng abis")

print(f"Terima kasih {nama}")
print("akhir dari program")

# 2. Program If dengan Indentasi
print("\n--- If dengan Indentasi ---")
if nama == "Ucup":
    print("Kamu ganteng abis")
    print("Kamu juga keren banget")

print(f"Terima kasih {nama}")
print("akhir dari program")

# 3. Program If-Else Statement
print("\n--- If-Else Statement ---")
nama_otong = input("Siapa nama anda untuk contoh If-Else? ")

if nama_otong == "Otong":
    print("Hai Otong, si keren")
else:
    print("Ah kamu bukan Otong, kamu nggak keren")

print("akhir dari program")