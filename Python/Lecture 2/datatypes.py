# Variable Name Conventions


# camelCase

areaOfRectangleAndOfIsAre = 24*1


# PascalCase

AreaOfCircle = 2 * 3.14 * 13 * 13


# snake_case

area_of_triangle = 1/2*(12*45)




# multiple values to multiple variables

num1 = num3 =  num2 = 25

# print(num1, num2 + num3)


# array / list

arrOfNums = [12, 324, 90, 18, 2000000] # list


# destructuring a list

value1, value2, value3, value4, value5 = arrOfNums

# print(value1, value2, value3, value4, value5)



# operators

x = "is" # string
y = 12 # integer or int

# print(x + y)

# concatenate or concatenation or concat

str1 = "hello"
str2 = " world"

final_str = str1 + str2     # we are concatenating two strings
# print(str1 + str2)


# global variables and how to define functions

def my_func():
    global k
    k = "this is not me" # local variable
    # print(k)

my_func()

k = "this is me"
# print(k)


# type of variables
from decimal import Decimal

y = Decimal(12.32123244332423232345354354353532) # float

# print(type(k)) # string or str
# print(type(y)) # integer or int
# print(type(y)) # integer or int
# print(y) # integer or int

# scientific numbers or notation
"""
    if you want to write a scientific number which is in 10 raise to power or scientific notation such as
    cm, km, you have to use E as for 10^
"""

h = 24E2
# print(h)


# Type Casting

m = int("12")

# print(type(m))

m = str(m)
# print(type(m))

y = 12


# multiline string

# COLLECTION DATA TYPES in Python
# 1. dictionary (obj in js)

student = {
    "name": "Talha",
    "age": 21,
    "city": "lahore",
    "batch": "python 4",
    "subjects": ["html", "css", "js", "python"],
    "marks": {
        "maths": 99.99,
        "physics": 100,
        "chemistry": 22,
        "biology": 55
    }
}

# print(arrOfNums)