x = 10
b = x

print(hex(id(x)))
print(hex(id(b)))


print(isinstance(1, int))
print(isinstance('1', str))
print(isinstance(1, (int, str)))
print(isinstance({}, (int, str)))
print(isinstance({}, (int, str, dict)))
