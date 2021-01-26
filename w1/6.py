x = "awesome"
print("Python is " + x)
a = 10
b = {'id':12}
print("Python is {}, {}, {}".format(x, a, b))
print("Python is {0}, {1}, {2}".format(x, a, b))
print("Python is {1}, {0}, {2}".format(x, a, b))
print("Python is {first}, {second}, {third}".format(first=x, second=b, third=a))
print(f"Python is {x}, {a * 2}, {b['id']}")
