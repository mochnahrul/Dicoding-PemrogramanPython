# ZFill untuk menambahkan nilai numerik berupa 0 di sebelah kiri sebuah angka atau string
# zfill()

# Penerapan zfill pada angka
angka = 5
print(str(angka).zfill(5))
angka = -0.45
print(str(angka).zfill(5))

# Penerapan zfill pada string
kata = "aku"
print (kata.zfill(5))