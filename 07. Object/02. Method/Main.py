# Class method adalah sebuah fungsi yang mengubah metode menjadi metode dari class
# Metode class menerima masukan class secara implisit sebagai argumen pertama yang secara konvensi diberikan nama cls
# class Kalkulator:
#   def f(self):
#     return "hello world"

#   @classmethod
#   def tambah_angka(cls, angka1, angka2):
#     return "{} + {} = {}".format(angka1, angka2, angka1 + angka2)

# k = Kalkulator()
# print(k.tambah_angka(1, 2))

# Static method adalah sebuah fungsi yang mengubah metode menjadi metode statis
# Metode statis tidak menerima masukan argumen pertama secara implisit
class Kalkulator:
  def f(self):
    return "hello world"

  @staticmethod
  def kali_angka(angka1, angka2):
    return "{} x {} = {}".format(angka1, angka2, angka1 * angka2)

k = Kalkulator()
print(k.kali_angka(2, 3))