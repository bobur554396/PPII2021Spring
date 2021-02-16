class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a >= 6:
      raise StopIteration
    
    x = self.a
    self.a += 1
    return x

my_num = MyNumbers()
it = iter(my_num)  # calling function __iter__ in the class
# print(next(it))  # calling function __next__ in the class
# print(next(it))  # calling function __next__ in the class
# print(next(it))  # calling function __next__ in the class
# print(next(it))  # calling function __next__ in the class
# print(next(it))  # calling function __next__ in the class
# print(next(it))  # calling function __next__ in the class

for i in it:
  print(i)
