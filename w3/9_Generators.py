# What is the Generator?

def gen():
  yield 1
  yield 2
  yield 3

it = gen()
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

def gen2():
  # return [0, 1, 2, 3, 4, 5, 6 ,7, 8 ,9]
  for i in range(10):
    yield i

it = gen2()

for num in it:
  print(num)