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


# global variables

k = "this is me"

def my_func():
    k = "this is not me"
    print(k)

my_func()

print(k)