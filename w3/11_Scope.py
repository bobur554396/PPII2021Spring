b = 10 # Global scope variable

def hello():
  x = 2  # Local scope variable
  print(b)
  def hi():
    print(x)
  hi()

# print(x) # x is not defined here

hello()
print(b)
