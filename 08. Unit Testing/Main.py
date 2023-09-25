# Unittest merupakan proses pengujian perangkat lunak yang memastikan setiap unit/fungsi dari program teruji

# Case 1
# import unittest

# class TestStringMethods(unittest.TestCase):
#   def test_strip(self):
#     self.assertEqual("www.dicoding.com".strip("c.mow"), "dicoding")

#   def test_isalnum(self):
#     self.assertTrue("c0d1ng".isalnum())
#     self.assertFalse("c0d!ng".isalnum())

#   def test_index(self):
#     s = "dicoding"
#     self.assertEqual(s.index("coding"), 2)
#     # cek s.index gagal ketika tidak ditemukan
#     with self.assertRaises(ValueError):
#       s.index("decode")

# if __name__ == "__main__":
#   unittest.main()

# Case 2
# import unittest

# def koneksi_ke_db():
#   print("[terhubung ke db]")
# def putus_koneksi_db(db):
#   print("[tidak terhubung ke db {}]".format(db))

# class User:
#   username = ""
#   aktif = False
#   def __init__(self, db, username):  # Using db sample
#     self.username = username
#   def set_aktif(self):
#     self.aktif = True

# class TestUser(unittest.TestCase):
#   def test_user_default_not_active(self):
#     db = koneksi_ke_db()
#     dicoding = User(db, "dicoding")
#     self.assertFalse(dicoding.aktif)  # Tidak aktif secara default
#     putus_koneksi_db(db)

#   def test_user_is_active(self):
#     db = koneksi_ke_db()
#     dicoding = User(db, "dicoding")
#     dicoding.set_aktif()  # Aktifkan user baru
#     self.assertTrue(dicoding.aktif)
#     putus_koneksi_db(db)

# if __name__ == "__main__":
#   unittest.main()

# Case 3 
# Menggunakan metode bawaan dari class TestCase, yakni metode setUp() dan tearDown()
import unittest

def koneksi_ke_db():
  print("[terhubung ke db]")
def putus_koneksi_db(db):
  print("[tidak terhubung ke db {}]".format(db))

class User:
  username = ""
  aktif = False
  def __init__(self, db, username):  # Using db sample
    self.username = username
  def set_aktif(self):
    self.aktif = True

class TestUser(unittest.TestCase):
  def setUp(self):
    self.db = koneksi_ke_db()
    self.dicoding = User(self.db, "dicoding")

  def tearDown(self):
    putus_koneksi_db(self.db)
  
  def test_user_default_not_active(self):
    self.assertFalse(self.dicoding.aktif)  # Tidak aktif secara default

  def test_user_is_active(self):
    self.dicoding.set_aktif()  # Aktifkan user baru
    self.assertTrue(self.dicoding.aktif)

if __name__ == "__main__":
  unittest.main()