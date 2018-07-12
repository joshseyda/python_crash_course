# Object Oriented Programming

class Employee:

  raise_amount = 1.04

  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.email = first + "." + last + "@email.com"
    self.pay = pay

  def full_name(self):
    return '{} {}'.format(self.first, self.last)

  def apply_raise(self):
    self.pay = int(self.pay * self.raise_amount)  

emp_1 = Employee("Josh","Sai",100000)
emp_2 = Employee("Test","User",50000)

# class variable
print(Employee.raise_amount)
print(Employee.__dict__)

# changes only emp_1 raise amount this defaults to class value, but can be anything
emp_1.raise_amount = 1.10

# instance properties 
print(emp_1.full_name())
print(emp_1.email)
# instance access of class variable
print(emp_1.raise_amount)
# instance's properties as a dictionary
print(emp_1.__dict__)

print("------")

print(emp_2.full_name())
print(emp_2.email)
print(emp_2.raise_amount)
print(emp_2.__dict__)

