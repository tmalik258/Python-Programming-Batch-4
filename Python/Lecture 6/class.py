# Define a class
class test:
    class_attributes = "I am a student of python programming"

# make a object of class
obj = test()
print(obj.class_attributes)

# 2
class MyClass :
     class_property = 42

     def class_method(self):
          return f"this is class method . class_property = {self.class_property}"
ob = MyClass()
print(ob.class_method())

# make a new class
class Counter :
     #make constructor
     def __init__(self):
          self.count = 0
    # make functions/methods
     def display(self):
          print(f"Count is : {self.count}")
     def increment(self):
          self.count +=1
          print("Value is Incremented")


# create objects of the class
c1 = Counter()
c2 = Counter()
c3 = Counter()

#call objects methods
c1.display()
c1.increment()
c1.increment()
c1.increment()
print("#")

c2.display()
c2.increment()
c2.increment()