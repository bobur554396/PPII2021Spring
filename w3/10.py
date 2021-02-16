def fib(limit):
  a, b = 0, 1
  while a < limit:
    yield a
    a, b = b, a + b

it = fib(100)

# for n in it:
#   print(n)

def fib2(n):
  a, b = 0, 1
  for _ in range(n):
    yield a
    a, b = b, a + b

it = fib2(100)
for i in it:
  print(i)
