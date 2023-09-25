# List adalah jenis kumpulan data terurut (ordered sequence)
# Serupa, namun tak sama dengan array pada bahasa pemrograman lainnya
# Bedanya, elemen list pada python tidak harus memiliki tipe data yang sama

x = [5, 10, 15, 20, 25, 30, 35, 40]
print(x[5])
print(x[-1])
print(x[3:5])
print(x[:5])
print(x[-3:])
print(x[1:7:2])

# Elemen pada list dapat diubah atau ditambahkan
x = [1, 2, 3]
x[2] = 4
print(x)

x = [1, 2, 3]
x[2] = 4
x.append(5)
print(x)

# Untuk menghapus item pada list
binatang = ["kucing", "rusa", "badak", "gajah"]
del binatang[2]
print(binatang)