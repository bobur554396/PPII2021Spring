def myfunc(n: str) -> int:
  return len(n)


x = map(myfunc, ('apple', 'banana', 'cherry'))
print(list(x))

def my_map(func, iterable):
  for item in iterable:
    yield func(item)
  

x = my_map(myfunc, ('apple', 'banana', 'cherry'))
print(list(x))

print(ord('A'))
print(ord('Z'))
print(ord('a'))
print(ord('z'))
print(chr(122))


print(list(range(1, 10, 2)))
