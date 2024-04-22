# In Python, there are two main types of loops: for loops and while loops.
# Task
# for loops
fruits = ['apple','banana','graphes']
for fruit in fruits:
    print(fruit)
   
# while loops
# while(condition)
# #loop body
    
counter = 1     
while counter <= 5:  
    print(counter)
    counter += 1 

def factorial (n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
print(factorial(5))

#Sum all the list elements by using both a loops

numbers = [1,2,3,4,5]
total = 0

for number in numbers:
    total += number
print("The sum using the for loop is: ", total) 

# Reverse the list by using  a loop.
list1 = [4,5,6,7,8]
reverse = []
for a in list1:
    reverse.insert(0, a)
print(list1)
print("The reversed number list :", reverse)

# Make a table of the given number with all possible loops
num = 2
z = 1 
while z <= 10:
    print(f"{num} x {z} = {num * z}")
    z +=1

# Find the largest number in a list by using both a loop
    
abc = [12,45,67,88,54,89,90]
largest = abc[0]
for n in abc[1:]:
    if n > largest:
        largest = n
print("The largest number in the list :",largest)

# Find the smallest number in a list by using both a loop while method

q = 0 
small = abc[0]
while q < len(abc) - 1:
    if abc[ q +1] < small:
        small = abc[q +1]
    q +=1
print(abc)
print("the smallest number", small)

# Dictionary Task with loops
# 1. Make an associative list (Dictionary) to store the name of 5 students and iterate with a for loop.