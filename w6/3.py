print(any([True, False, False]))
print(any([0, False, False]))
print(any([0, 0, 0]))

def my_any(iterable):
  for item in iterable:
    if item:
      return True
  return False


print(my_any([True, False, False]))
print(my_any([0, False, False]))
print(my_any([0, 0, 0]))
