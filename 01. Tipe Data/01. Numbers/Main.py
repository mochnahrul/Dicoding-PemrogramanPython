# Numbers adalah tipe numerik pada python
# Tipe numerik pada python dibagi menjadi 3: int, float dan complex

# Integer -> Tidak dibatasi oleh angka atau panjang tertentu
a = 10
print(a, "bertipe", type(a))

# Float -> Dibatasi akurasinya pada 15 desimal
b = 1.7
print(b, "bertipe", type(b))

# Complex -> Bilangan imajiner dan bilangan kompleks
# Formulasi x + yj, yakni bagian x adalah bilangan real dan y adalah bilangan imajiner
c = 1+3j
print(c, "bertipe bilangan kompleks?", isinstance(1+3j, complex))