# Object Oriented Programming

class Employee:

  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.email = first + "." + last + "@email.com"
    self.pay = pay

emp_1 = Employee("Josh","Sai",100000)
emp_2 = Employee("Test","User",50000)

"""
emp_1.first = "Josh"
emp_1.last = "Sai"
emp_1.email = "josh.sai@email.com"
emp_1.pay = 100000

emp_2.first = "Test"
emp_2.last = "User"
emp_2.email = "test.user@email.com"
emp_2.pay = 50000

print(emp_1.email)
print(emp_2.email)

"""

print(emp_1.email)
print(emp_2.email)