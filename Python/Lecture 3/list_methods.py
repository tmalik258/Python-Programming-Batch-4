# Initialize a list 
my_list = [1,22,2,3,4,5,0.5,6,7,8,9]
# display the list
print("Lists = ",my_list)

# List Methods
# 1 . append () Add an element at the end of the list
my_list.append(10)
print("After append element = ",my_list)

# 2. Extend () adds a element from another list
my_list.extend([11,12,13])
print("After use the extend method", my_list)

# 3. Insert Method insert a element in the specific position
my_list.insert(5, 5.5)
print("After the use the method insert = ", my_list)

# 4. Remove  method
my_list.remove(5.5) 
print("After use the remove method =", my_list)

# 5 . Pop method  removes the element at the specified position
pop_element = my_list.pop(5)
print("After use the pop method  = ", my_list)
print("Poped element = ", pop_element)

# 6. Index Method return the index of the first matching element
print("Index of 7",my_list.index(7))

# 7. Count method  returns 
count = my_list.count(9)
print("Total list", my_list)
print("Print Count in the lists =", count)

# 8. Sort method
my_list.sort()
print("Sorted List", my_list)

# 9 . Reverse Method
my_list.reverse()
print("Reverse lists : ", my_list)