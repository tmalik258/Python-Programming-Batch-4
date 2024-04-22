# Define a tuple
my_tuple = (1,"apple",3.14 )

# Expalanation
# tuples are created using the paraentheses () and sperated-comma ,

# Case 1 : Accessing a element in a tuple
print("First Element :", my_tuple[0])
print("Second Element :",my_tuple[1])

# Note that python indexing starts at 0

# Case 2 Length of the tuple
print("Length of the tuple is : ", len(my_tuple))

# Case 3 Slicing a tuple
print("Slicing my tuple (element 1-2)", my_tuple[1:3])

# Case 4 Count METHOD
print("Number of apple in tupple:", my_tuple.count("apple"))

# Case 5 Index
print("Index of the 3.14 in mytupple:" , my_tuple.index(3.14))

# Case 6 Tupples Method
print("Methods of the tuples", dir(my_tuple))

# Case 7 Immutablity of tupples
try:
 my_tuple[1] = "oranges"
except TypeError as e:
 print(e)
