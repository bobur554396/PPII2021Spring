# function
def hello():
  print('hello pp2')

def square(a):
  print(a * a)

def sum(a, b):
  print(a + b)

# square(4)
# sum(a=2, b=4)

def f1(*args):
  # print(args)
  for arg in args:
    print(arg)

# f1(1, 'hello', {'id': 123}, True)

def f2(a, b, *args):
  print(a, b)
  for arg in args:
    print(arg)

# f2(2, 3, 'hello', True, 2.4)

def f3(name, age):
  print(f'{name} -> {age}')

# f3(name='Student1', age=20)

def f4(name, age, **kwargs):
  print(f'{name} -> {age}')
  # print(kwargs)
  # print(kwargs['gpa'], kwargs['year'], kwargs['faculty'])
  for key in kwargs:
    print(f'{key} => {kwargs[key]}')

# f4(name='Student 1', age=20, gpa=3.9, year=2, faculty='FIT')

def f5(name, age=18): # default value
  print(f'{name} -> {age}')

# f5('Student 1', 20)

def f6(nums):
  for i in nums:
    print(i * 2)

# a = [2, 4, 5]
# f6([2, 4, 5])

