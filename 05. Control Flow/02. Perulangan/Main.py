# While
# count = 1
# while (count < 7):
#   print("Hitungannya adalah:", count)
#   count += 1

# For
# for huruf in "Dicoding":
#   print("Huruf:", huruf)

# flowers = ["mawar", "melati", "anggrek"]
# for flower in flowers:
#   print("Flower:", flower)

# Berdasarkan index atau range
# flowers = ["mawar", "melati", "anggrek"]
# for index in range(len(flowers)):
#   print("Flowers:", flowers[index])

# Perulangan bersarang
pattern = ""
for i in range(0, 4):
  for j in range(0, i+1):
    pattern += "*"
  pattern += "\n"
print(pattern)