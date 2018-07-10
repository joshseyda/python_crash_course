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

# Bitwise Operators, convert to bits then does operation

num4 = 6 #110
num5 = 2 #010

# returns 2 because there are 2 0s?
print("Bitwise AND", num4&num5)
# returns 6 because there are 2 11s?
print("Bitwise OR", num4|num5)
# returns 4
print("Bitwise XOR", num4^num5)
# shift left by x bits
print(3 << 2) # =12 0011 becomes 1100
# shift right by x bits
print(3 >>2) # =0 0011 becomes 0000

# Identity operators!

x = 5
print(x is 5) # true
print(x is not 5) # false

# Membership operators

x = [1, 2, 3, 4, 5]

print(3 in x) #true
print(3 not in x) #false

