a = [1, "2", True, {'a': 11}, 1.5]
b = list((1, 2, 3))
print(type(a))
print(type(b))

print(len(a))
print(a[len(a) - 1])
print(a[-1])
print(a[1:4]) # [start:end:step]

a[0] = {'id': '20BD123123'}
a[1] = ['a', 'b', 'c']

a.append("hello")
a.append("hello")

print(a)



