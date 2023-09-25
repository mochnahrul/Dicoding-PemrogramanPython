# def angka(args):
#   for i in range(len(args)):
#     print(args[i])

# angka([1, 2])

# var-positional dan var-keyword
def printinfo(*args, **kwargs):
  for a in args:
    print("Argumen posisi", a)
  for key, value in kwargs.items():
    print("Argumen kata kunci {}:{}".format(key, value))

printinfo(1, 2, 3)
printinfo(i=7, j=8, k=9)
printinfo(1, 2, j=8, k=9)
printinfo(*(2, 3), **{"i":7, "j":8})