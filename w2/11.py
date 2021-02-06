thistuple = tuple(("apple", "banana", "cherry"))
a = list(thistuple)
a[0] = 1
thistuple = tuple(a)
# thistuple[0] = 1
# print(a)
print(thistuple)
