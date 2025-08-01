# Write External Data

'''
Ketika membuat program Write, secara otomatis jika tidak ada file
sebelumnya maka akan membuat file. Dan akan menimpa atau overwrite ketika 
'''

with open("data_01.txt",mode="w",encoding="utf-8") as file:
    file.write("data ke 01\n")

with open("data_01.txt",'w',encoding="utf-8") as file:
    file.write("ucup surucup")

with open("data_01.txt",'w',encoding="utf-8") as file:
    file.write("overwrite")

# Mode Append 

'''
Akan menambah isi dari file setiap kali program di jalankan.
'''

with open("data_02.txt",'w',encoding="utf-8") as file:
    file.write("Apend_01")
    
with open("data_02.txt",'a',encoding="utf-8") as file:
    file.write("Apend_02")

with open("data_02.txt",'a',encoding="utf-8") as file:
    file.write("Apend_03")

# Mode r+

'''
Akan menimpa/overwrite isi dari file sesuai panjang dari data yang di input.
Mode ini tidak akan berjalan jika tidak ada file yang di temukan.
'''

with open("data_03.txt",'w',encoding="utf-8") as file:
    file.write("Data Awal")
    
with open("data_03.txt",'r+',encoding="utf-8") as file:
    file.write("over")
    file.write("overwrite")
    file.write("overwrite")

with open("data_03.txt",'r+',encoding="utf-8") as file:
    data = file.read()
    print(data)
