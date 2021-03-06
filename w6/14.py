a = ['a', 'b', 'c', 'd']
index = [1, 2, 3]
c = (11, 22, 33, 55)

print(list(zip(a, index, c)))

for a, b, c in zip(a, index, c):
  print(f'{a} -> {b} -> {c}')


# TODO homework
def my_zip():
  pass