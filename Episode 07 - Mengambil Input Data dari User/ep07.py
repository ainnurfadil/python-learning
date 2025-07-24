# Mengambil input data dari user menggunakan input()

data = input("masukkan data: ")
print("hasil masukkan : ", data, "type data : ", type(data)) # type data yang dihasilkan dari inputan adalah string walaupun yang di input adalah angka

# Untuk mengambil data integer, maka harus di casting dulu ke integer

angka = int(input("masukkan data integer : "))      # sifatnya akan sama ketika mengcasting type datanya
angka = float(input("masukkan data angka : "))      # sifatnya akan sama ketika mengcasting type datanya

print("hasil masukkan :", angka, "type data :", type(angka))

# Menginput data boolean (True atau False)
# Ketika mengambil data boolean akan sedikit tricky, karena data inputan harus di ganti ke integer

boolean = bool(int(input("masukkan nilai boolean : "))) 

print("hasil masukkan :", boolean, "type data :", type(boolean)) 


