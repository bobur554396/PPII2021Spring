class Person:
  name = 'Person 1'
  age = 20

  @classmethod
  def samle(cls, gpa):  # class method
    print(gpa)

  def get_age(self):  # instance method
    return self.age
  
  def __str__(self):
    return f'Person: {self.name}, {self.age}'

p = Person()

print(p)

print(getattr(p, 'age'))
print(getattr(p, 'name'))
print(getattr(p, 'gpa', 3.8))

print(hasattr(p, 'age'))
print(hasattr(p, 'asd'))

setattr(p, 'age', 22)
print(getattr(p, 'age'))

delattr(Person, 'age')
p1 = Person()
print(getattr(p1, 'age', 'default age'))

# print(dir(p))

x = 10
print(dir(x))
