fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)

l = [x for x in fruits if 'a' in x]
print(l)


# newlist = [x for x in fruits]
# newlist = fruits.copy()
newlist = list(fruits)

print(id(fruits))
print(id(newlist))
print(fruits)
print(newlist)

print([x.capitalize() for x in fruits])

print(['hello' for x in fruits])
