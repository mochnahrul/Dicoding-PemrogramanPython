# Class merupakan sintaksis di Python yang menyediakan semua fitur-fitur standar dari OOP

# class Kalkulator:
#   i = 12345

#   def f(self):
#     return "hello world"

# k = Kalkulator()
# print(k.f())

# Class Constructor
class Kalkulator:
  def __init__(self, i=12345):
    self.i = i

  def f(self):
    return "hello world"

k = Kalkulator(i=1024)
print(k.i)