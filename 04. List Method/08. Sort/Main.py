# Sort untuk mengurutkan angka atau urutan huruf
# sort()

angka = [100, 1000, 500, 200, 5]
angka.sort()
print(angka)

# Menjadikan urutannya terbalik
angka = [100, 1000, 500, 200, 5]
angka.sort(reverse=True)
print(angka)

# Membuat metode sort menganggap semua objek menggunakan huruf kecil
kendaraan = ["Motor", "Mobil", "helikopter", "pesawat"]
kendaraan.sort(key=str.lower)
print(kendaraan)