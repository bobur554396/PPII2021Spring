# print(all([True, True, True]))
# print(all([True, False, True]))

# print(all([1, 10, 12]))
# print(all([1, 10, 0]))

# print(all((1, 4, 'hello')))
# print(all('hello'))
# print(all(''))

def my_all(iterable):
  for item in iterable:
    if not item:
      return False
  return True


print(my_all([True, True, True]))
print(my_all([True, False, True]))

print(my_all((1, 0, 'hello')))
print(my_all('hello'))
print(my_all(''))
