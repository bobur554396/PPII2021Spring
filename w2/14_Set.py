myset = {"apple", "banana", "cherry", "apple"}
a = set()
print(type(myset))
print(type(a))

print(myset)
print(len(myset))

# thisset = set(("apple", "banana", "cherry"))
# print(thisset)

myset.add('orange')
myset.add('orange')
myset.add('orange')
for i in myset:
  print(i)

