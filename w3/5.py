class Person:
  # constructor
  def __init__(self, n, a):
    # print('Person class constructor called')
    self.name = n
    self.age = a
  
  def show(self):
    print(f'{self.name} -> {self.age}')
  

p = Person('Person1', 20)
# print(p.name)
# print(p.age)
p.show()

# del p
