print(bool(2))
print(bool('2'))
print(bool([1]))
print(bool({'a': 1}))
print(bool(True))
print(bool((1,)))

print('-' * 50)

print(bool(()))
print(bool([]))
print(bool({}))
print(bool(0))
print(bool(False))
print(bool(None))
print(bool(''))

print('-' * 50)

def is_even(n): # snake case
  return n % 2 == 0

print(is_even())
