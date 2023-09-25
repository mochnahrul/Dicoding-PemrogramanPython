class Kalkulator:
  def __init__(self, nilai=0):
    self.nilai = nilai

  def tambah_angka(self, angka1, angka2):
    self.nilai = angka1 + angka2
    if self.nilai > 9:
      print("kalkulator sederhana melebihi batas angka: {}".format(self.nilai))
    return self.nilai

class KalkulatorKali(Kalkulator):
  # Menimpa (override) method dengan nama yang sama dengan kelas dasar
  # def tambah_angka(self, angka1, angka2):
  #   self.nilai = angka1 + angka2
  #   return self.nilai

  # Pemanggilan method kelas dasar dari kelas turunan dengan sintaksis super
  def tambah_angka(self, angka1, angka2):
    if angka1 + angka2 <= 9:
      super().tambah_angka(angka1, angka2)
    else:
      self.nilai = angka1 + angka2
    return self.nilai

  def kali_angka(self, angka1, angka2):
    self.nilai = angka1 * angka2
    return self.nilai

kk = KalkulatorKali()
print(kk.tambah_angka(5, 5))
print(kk.kali_angka(5, 5))