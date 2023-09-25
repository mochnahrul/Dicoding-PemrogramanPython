# Strings adalah urutan dari karakter unicode yang dideklarasikan dengan petik tunggal atau ganda
# String > 1 baris dapat ditandai dengan tiga petik tunggal atau ganda ''' atau """"

s = "Ini adalah string baris tunggal"
print(s)

s = '''Ini adalah string
yang memiliki baris pertama
dan selanjutnya baris kedua'''
print(s)

# Slicing [] -> Mengambil isi pada string/substring

s = "Hello World!"
print(s[4])
print(s[6:11])

s = "Halo Dunia!"
print(s)

# String Literals

# Escape Character:
# - \' Single Quote
# - \" Double Quote
# - \t Tab
# - \n Newline
# - \\ Backslash
print("Halo!\nKapan terakhir kali kita bertemu?\nKita bertemu hari Jum\'at yang lalu.")

# Raw Strings -> Mencetak string sesuai dengan apa pun input atau teks yang diberikan

print(r"Dicoding\tIndonesia")