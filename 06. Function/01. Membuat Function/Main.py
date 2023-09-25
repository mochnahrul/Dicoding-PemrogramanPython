import math

def jumlahVolumeKubus(a, b):
  volumeA = math.pow(a, 3)
  volumeB = math.pow(b, 3)
  return volumeA + volumeB

print(int(jumlahVolumeKubus(8, 3)))

# Function Lambda
# tambah = lambda angka1, angka2: angka1 + angka2
# print(tambah(5, 5))