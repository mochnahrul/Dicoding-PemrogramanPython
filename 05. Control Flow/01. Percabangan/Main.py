# If
# kelerengku = 10
# if kelerengku:
#   print ("Cetak ini jika benar")
#   print (kelerengku)

# Else
# tinggi_badan = int(input("Masukkan tinggi badan Anda : "))
# if tinggi_badan>=160:
#   print ("Silakan, Anda boleh masuk")
# else:
#   print ("Maaf, Anda belum boleh masuk")

# Elif
nilai = int(input("Masukkan nilai tugas Anda : "))
if nilai > 80:
  print("Selamat! Anda mendapat nilai A")
  print("Pertahankan!")
elif nilai > 70:
  print("Hore! Anda mendapat nilai B")
  print("Tingkatkan!")
elif nilai > 60:
  print("Hmm.. Anda mendapat nilai C")
  print("Ayo semangat!")
else:
  print("Waduh, Anda mendapat nilai D")
  print("Yuk belajar lebih giat lagi!")