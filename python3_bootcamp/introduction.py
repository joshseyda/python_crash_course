# floats take up more space than whole numbers
#  this document will be a brief review of data types, and basic concepts in python

# basic variable declaration
khaleesi_mother_of_dragons = 1
x = 100
print(khaleesi_mother_of_dragons + x ) # 101

# variable names must start with a letter or underscore, and can contain lettes numbers or underscores, thats it!
# names are also CASE sensitive ~ and are generally written in snake_case
# most variables are lowercase, if all caps that denotes its value is constant
PI = 3.141592654
# UpperCamelCase refers to a class
# variables that start and end with dunder(double underscore) are supposed to be private or left alone
__no_touchy__ = 0

# other data types out here...
# bool, int, str, list, dict, None
#  list is an array
# dictionary is a hash

# python is a dynamic typed language, meaning NO TYPE DECLARATIONS!

# double vs single quotes
# it doesnt matter as long as you are consistent

# string escape characters/sequences
# to make a return inside a string \n
# \\ adds a backslash
# there are others, check  the docs for RegEx solutions

# string concatenation! 
str_one = "ahoy"
str_two = "yoha"
str_three = str_one + " " + str_two
print(str_three)
str_four = "hayo"
str_three += str_four
print(str_three)

# string interpolation
# the f in front of the string is the command for an interpolated string
# the {} contains something outside of the string, you can do math inside of it and it returns a string
x = 10
formatted = f"I've told you {x} times already!"
print(formatted)
# you can also do the older way..
formatted_0 = "I've told you {} times already!".format(10)
# super deprecated way to do this
formatted_00 = "I'be told you %d times already!" % (x)

# strings can have indexes!
str_thing = "lol"
str_thing[0] # => "l"
str_thing[-2] # => "o"

# converting data types
decimal = 12.2534
integer = int(decimal) #12
my_list = [1, 2, 3]
my_list_as_a_string = str(my_list) # "[1, 2, 3]"







