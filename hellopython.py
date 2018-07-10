import random
import sys
import os

print('Hello Python!')

# single line 
"""
 multi line comment
"""

name = "Josh"
exclamation = "!"

# new names for data types .... List, Tuple, Map, Dictionary

print("%s %s %s" % ("Hi my name is ", name, exclamation))

#  // is used to truncate the result of division ie 7/3 = 2

# Assignment operators
x=5
print(x)

x/=5
print(x)

x=5
x%=5
print(x)

x=5
x//=2
print(x)

x=5
x**=5
print(x)

#  Logical Operators

truValue = True 
falValue = False
# both must be true
print("X and Y", truValue and falValue)
# either can be true
print("X or Y", truValue or falValue)
# returns the opposite of the variable
print("not of X", not truValue)



