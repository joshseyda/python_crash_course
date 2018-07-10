# Data Types in Python
# There are Immutable and Mutable Data Types

'''
Immutable data types are Numbers, Strings, and Tuples.
Mutable data types are Lists, Dictionaries, and Sets.
Each of these Data Types has specific properties we will explore below
'''

# Numeric Data
# Integer
4
# Float
3.5
# Complex (imaginary number i is j in python!)
4+4j

# Strings
"This is a string"
'thisisalsoastring'
''' this
is 
a multi
line string
'''

# slice a string
string1 = "Edureka"
str1 = "E, d, u, r, e, k ,a"
print(string1[2:7])#ureka
print(string1[-1]+string1[1])#ad

#  Type Specific Method
string1="Edureka"
# .find()
print(string1.find("ureka"))#2
# .replace()
print(string1.replace("Ed", "E"))# Eureka
# .split()
print(str1.split(',')) # ['E', 'd', 'u', 'r', 'e', 'k', 'a']
# .count()
print(string1.count('e', 0, 6))
# .upper()
print(string1.upper()) #EDUREKA
# max() returns letter highest in the alphabet
print(max(string1)) #u
# min() returns letter lowest in alphabet
print(min(string1)) #a actually returns E because of case?!
# .isalpha() verifies if string is made of letters
print(string1.isalpha()) #true
print(string1.isalnum())
print(string1.isdecimal())
print(string1.isdigit())
print(string1.isnumeric())
# etc!!!!!


# Tuples > sequence of immutable objects, can't be changed (unlike lists), defined using parenthesis

myTuple =("Python", 2.4, 6, "!")
myTuple+=(1, 2, 3)
print(myTuple)
print(myTuple*3)
print(myTuple[2:4])
print(myTuple[4])


#  Lists > sequence o mutable objects, can be modified, defined with square braces like Arrays!

myList = ["JavaScript", "Python", 3.1415, "coding is fun!"]

# concatenation, repitition, slicing, and indexing are all done the same as tuples..
# type specific methods for lists
myList.append("Django!")
print(myList)
myList.extend(["this is", "another List"])
print(myList)
myList.insert(2, "Ruby is like Python?!")
print(myList)
myList.pop()
print(myList)

