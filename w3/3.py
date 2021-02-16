# lambda function
x = lambda a : a + 10
# print(x(5))

s = lambda a, b : a + b

# print(s(2, 4))

def fun(n):
  return lambda x : x * n

doubler = fun(2)
# print(doubler(20))
# print(doubler(5))

tripler = fun(3)
print(tripler(4))
print(tripler(20))


aa = fun(12)
print(aa(10))
