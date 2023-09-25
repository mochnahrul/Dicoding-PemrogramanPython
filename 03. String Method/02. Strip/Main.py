# Strip untuk menghapus ruang kosong dan menghilangkan sebuah karakter

# rstrip() -> Menghapus whitespace pada sebelah kanan string atau akhir string
print("Dicoding    ".rstrip())

# lstrip() -> Menghapus whitespace pada sebelah kiri string atau awal string
print("    Dicoding".rstrip())

# strip() -> Menghapus whitespace pada bagian awal atau akhir string
print("    Dicoding    ".strip())
# Menentukan mana karakter atau bagian yang ingin dihilangkan
kata = "CodeCodeDicodingCodeCode"
print(kata.strip("Code"))