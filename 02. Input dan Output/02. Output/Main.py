# Memasukan nilai variabel pada string
x = 100
print("Nilai x adalah", x)

# Menggunakan mekanisme string format
print("hai {}".format("bro"))

# Menggunakan operator "%" yang ditambahkan dengan "argument specifiers"
# Argument Specifiers:
# - %s -> String
# - %d -> Integers
# - %f -> Bilangan Desimal
# - %.<digit>f -> Bilangan desimal dengan sejumlah digit angka dibelakang koma
# - %x/%X -> Bilangan bulat dalam representasi Hexa (huruf kecil/huruf besar)
nama = "Dicoding"
umur = 5
print("Umur %s adalah %d tahun." % (nama, umur))