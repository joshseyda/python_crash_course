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

my_tuple =("Py_thon", 2.4, 6, "!")
my_tuple+=(1, 2, 3)
print(my_tuple)
print(my_tuple*3)
print(my_tuple[2:4])
print(my_tuple[4])


#  Lists > sequence o mutable objects, can be modified, defined with square braces like Arrays!

my_list = ["JavaScript", "Python", 3.1415, "coding is fun!"]

# concatenation, repitition, slicing, and indexing are all done the same as tuples..
# type specific methods for lists
my_list.append("Django!")
print(my_list)
my_list.extend(["this is", "another List"])
print(my_list)
my_list.insert(2, "Ruby is like Python?!")
print(my_list)
my_list.pop()
print(my_list)

# Dictionaries > most flexible data type, collection of key value pairs in curly braces like a hash

my_dict = {1: "josh", "steve": [1, 5, 7], 2: "danielle"}

# dictionary methods

print(my_dict[1]) #"Josh"
print(len(my_dict)) #3
print(my_dict.keys()) # [ 1 , 'steve', 2]
print(my_dict.values()) #['josh', [1, 5, 7], 'daniele']
print(my_dict.items()) #[(1, 'josh), (steve, [1, 5, 7]), (2, 'daniele')]
print(my_dict.get(1)) # 'josh'
my_dict.update({3:"barbeque"}) # {1: "josh", "steve": [1, 5, 7], 2: "danielle", 3: "barbeque"}
print(my_dict) 
print(my_dict.pop(2)) # 'danielle'
print(my_dict) # {1: "josh", "steve": [1, 5, 7], 3: "barbeque"}

#  Sets > unordered collection of items, every element is unique, no duplicates, and they are immutable

my_set = {1, 1, 2, 3, 5}
print(my_set) # {1, 2, 3 ,5}
my_other_set = {8, 13, 21, 34}
my_other_other_set = {2,4,5,6}
# sets methods
# union
my_new_set = my_set|my_other_set
print(my_new_set) # {1,2,3,5,8,13,21,34}
# intersection
my_smaller_set = my_set & my_other_other_set
print(my_smaller_set) # {2, 5}
# difference
my_last_set = my_set - my_other_other_set #removes the items in my_other_other_set from my_set, if they are already absent, nothing happens!
print(my_last_set) # {1, 3}
