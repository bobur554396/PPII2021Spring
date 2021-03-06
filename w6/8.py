print(divmod(13, 5)) # (int(a / b), a % b)

def my_divmod(a, b):
  return (int(a / b), a % b)

l = ['a', 'b', 'c']
# print(list(enumerate(l)))
# print(list(enumerate(l, start=1)))

# for index, val in enumerate(l):
#   print(f'{index} -> {val}')


def my_enumerate(iterable, start=0):
  n = start
  for item in iterable:
    yield n, item
    n += 1

# print(list(my_enumerate(l)))
for index, val in my_enumerate(l, 10):
  print(f'{index} -> {val}')
