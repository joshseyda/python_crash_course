# conditional logic to make decisions!
# if elif else
name = input("What is your name?: ")
if name == "Arya Stark":
  print("Valar Morghulis")
elif name == "Jon Snow":
  print("You know nothing")
elif name == "Daenerys Targaryen":
  print("The Unburnt, The Breaker of Chains, The Mother of Dragons")
else:
  print("Carry on!")

# truthiness in Python
x = 1
x is 1 # true
x is 2 # false
# empty strings, None, and 0 are all falsey values
# everything else is truthy by default
#  < > != == >= <= do all of the things you'd expect..
# and or not
# and is for two conditions both being true
# or is for one of two being true
# not is for both being false

# is versus ==
# is is checking if both objects are stored in the same place in memory
#  == is evaluating if the values are the same



