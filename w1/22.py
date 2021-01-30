a = [2, 3, 4]
b = a  # a.copy()

# b.append(5)
# a.append(6)

c = [2, 3, 4]
print(hex(id(a)))
print(hex(id(b)))
print(hex(id(c)))

print(a == b)
print(a is b)
print(a is c)
