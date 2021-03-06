def hello():
  print('hi')

print(callable(hello))

class Person:
  name = 'Person 1'
  age = 20

  @classmethod
  def samle(cls, gpa): # class method
    print(gpa)

  def get_age(self): # instance method
    return self.age

p = Person()

p.get_age() #-> p.get_age(p)

print(callable(Person))
print(callable(p))
print(callable(p.get_age))

print(chr(97))
print(chr(122))
print(chr(65))
