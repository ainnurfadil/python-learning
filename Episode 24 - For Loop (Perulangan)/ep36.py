list_buku = [] # List utama untuk menyimpan semua dictionary buku

while True:
    print("\n--- Masukkan Data Buku ---")
    judul = input("Masukkan judul buku: ")
    penulis = input("Masukkan nama penulis: ")

    buku_baru = [judul, penulis] # Setiap buku adalah list kecil
    list_buku.append(buku_baru) # Tambahkan buku ke list utama

    # Menampilkan daftar buku
    print("\n--- Daftar Buku ---")
    if not list_buku:
        print("Belum ada buku dalam daftar.")
    else:
        print("No.\t| Judul Buku\t\t| Nama Penulis")
        print("--------------------------------------------------")
        for i, buku in enumerate(list_buku):
            # Mengatur lebar kolom agar rapi (asumsi judul/penulis tidak terlalu panjang)
            # Contoh sederhana, bisa disempurnakan dengan f-string padding lebih kompleks
            judul_print = buku[0][:20].ljust(20) # Potong jika terlalu panjang, rata kiri
            penulis_print = buku[1][:20].ljust(20)

            print(f"{i+1}.\t| {judul_print}\t| {penulis_print}")
        print("--------------------------------------------------")

    # Konfirmasi lanjut atau tidak
    is_lanjut = input("\nLanjutkan memasukkan data (Y/N)? ").lower()
    if is_lanjut == 'n':
        break
