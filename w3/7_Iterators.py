# - [ ] What is iterator?
# - [ ] Iterator vs Iterable
# Iterable -> all collections -> List, Tuple, Set, Dict
# Iterator -> objects to iterate over
a = [1, 2, 3]
myit = iter(a)
# print(myit)

# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))

for i in myit:
  print(i)