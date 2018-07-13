# Object Oriented Programming
import datetime

class Employee:
  # variable scoped to the class only
  num_of_employees = 0
  # variable scoped to the class but open to change on the instance
  raise_amount = 1.04

  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.email = first + "." + last + "@email.com"
    self.pay = pay
    Employee.num_of_employees+=1

  def full_name(self):
    return '{} {}'.format(self.first, self.last)

  def apply_raise(self):
    self.pay = int(self.pay * self.raise_amount)  

  @classmethod 
  def set_raise_amount(cls, amount):
    cls.raise_amount = amount
  
  @classmethod
  # method to parse string formatted as "First-Last-Pay" to create new instances
  def from_string(cls, emp_str):
    first, last, pay = emp_str.split("-")
    return cls(first, last, pay)

  # static methods are used for when you do not need to access the class or the instance itself to do the operation
  @staticmethod
  def is_workday(day):
    if day.weekday() == 5 or day.weekday() == 6:
      return False
    return True

# creating subclasses
class Developer(Employee):
  raise_amount = 1.10

  def __init__(self, first, last, pay, prog_lang):
    super().__init__(first,last,pay)
    self.prog_lang = prog_lang

class Manager(Employee):

  def __init__(self, first, last, pay, employees=None):
    super().__init__(first,last,pay)
    if employeesis None:
      self.employees = []
    else:
      self.employees = employees

  def add_employee(self, emp):
    if emp not in self.employees:
      self.employees.append(emp)

  def remove_employee(self, emp):
    if emp in self.employees:
      self.employees.remove(emp)
  
  def print_emps(self):
    


emp_1 = Employee("Josh","Sai",100000)
emp_2 = Employee("Test","User",50000)
dev_1 = Developer("Linus", "Torvalds", 120000, "C")
print(dev_1.__dict__)

# print(help(Developer)) # this gives you a bunch of useful info!
# # class variable
# print(Employee.raise_amount)
# print(Employee.__dict__)

# # changes only emp_1 raise amount this defaults to class value, but can be anything
# emp_1.raise_amount = 1.10

# # instance properties 
# print(emp_1.full_name())
# print(emp_1.email)
# # instance access of class variable
# print(emp_1.raise_amount)
# # instance's properties as a dictionary
# print(emp_1.__dict__)

# print("------")

# print(emp_2.full_name())
# print(emp_2.email)
# print(emp_2.raise_amount)
# print(emp_2.__dict__)

# print("------")

# print(Employee.num_of_employees)
# # changes all employee raise amounts
# Employee.set_raise_amount(1.08)
# # check to see its effects...
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# # still works to edit individual instances
# emp_1.raise_amount = 1.10
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# emp_str_1 = "Aimee-Cesaire-120000"
# emp_3 = Employee.from_string(emp_str_1)
# print(emp_3.__dict__)

# my_date = datetime.date(2018,2,16)
# print(Employee.is_workday(my_date))