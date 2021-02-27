f = open('file1.txt', 'r')
# print(f)
# print(type(f.read()))
# print(f.read())

# print(f.readline())
# print(f.readline())


# print(f.readlines())

# for line in f.readlines():
#   print(len(line))

for line in f:
  print(line)

f.close()
