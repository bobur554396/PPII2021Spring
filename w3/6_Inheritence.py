# - [ ] What is class Inheritance?

class Person:
  def __init__(self, _name, _age):
    self.name = _name
    self.age = _age

  def show(self):
    print(f'{self.name} -> {self.age}')


# Person - Parent class / Base class
# Student - Child class / Derived class
class Student(Person): 

  def __init__(self, _name, _age, _gpa, _faculty):
    # Person.__init__(self, _name, _age)
    super().__init__(_name, _age)
    self.gpa = _gpa
    self.faculty = _faculty

  def show(self):
    super().show()
    print(f'{self.gpa} -> {self.faculty}')

s = Student('Student 1', 20, 3.9, 'FIT')
s.show()

