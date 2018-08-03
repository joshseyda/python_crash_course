# code along with nested conditionals
# ask for age
# age is 18-21
# if 21+ normal entry, if <18 too young to enter
age = input("How old are you: ")
if age:
  age = int(age)
  if age >= 18 and age < 21:
    print("You can enter, but you need an underage wristband!")
  elif age > 21:
    print("Come on in, you can order drinks at the bar")
  else:
    print("You are too young to enter the concert")
else:
  print("Enter your age or your not going into the concert!")