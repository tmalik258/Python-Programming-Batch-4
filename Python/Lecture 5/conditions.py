# Condition in Python 
#Logical

# if condition
# a = 45
# b = 44
# if b > a:
#     print("B is greater than a")
# elif a == b :
#     print("a is equal to b")
# else :
#     print("a is greater than b")

# short hand if 
# if a>b : print("a is greater than b")

# short hand if else
# x = 23
# y = 200
# print("X") if x > y else print("Y") 

# short hand condition if else with 3 conditions
q = 330
w = 330
print("Q") if q>w else print("=") if q == w else print("W")

# Logical Operator
# and
abc = 200
xyz = 30
qwe = 20

if abc>xyz and abc>qwe:
    print("Greater number")

# OR operator
# a = 700
# b = 33
# c = 500
# if a>b or a>c:
#     print("A is greater")
# else:
#     print("A is not greater than ")

# Not Operator
a = 33
b = 200 
if not a > b:
    print("A is not greater than b")

# Nested If

x = 42
if x> 10:
    print("Above ten")
    if x> 20:
        print("and also above 20")
    else:
        print('But not above 20')

# Task 
# # #  Check whether a given number is even or odd.
# # num % 2 == 0