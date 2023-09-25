# Replace untuk mengganti elemen string

# replace() -> Mengembalikan string baru dalam kondisi substring telah tergantikan
string = "Ayo belajar Coding di Dicoding"
print(string.replace("Coding", "Pemrograman"))

# Parameter ketiga pada replace dapat diisi jumlah substring yang ingin diganti
string = "Ayo belajar Coding di Dicoding karena Coding adalah bahasa masa depan"
print(string.replace("Coding", "Pemrograman", 1))