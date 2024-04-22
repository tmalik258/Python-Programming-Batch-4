class Person(): # parent class or base class
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # method
    def speak(self):
        print('I am speaking')
    
    def print_name(self):
        print(f'My name is {self.name}')


# inheritance

class Student(Person): # child class or derived class
    def __init__(self, name, age, gender, grde, section, sbj):
        super().__init__(name, age, gender)
        self.grade = grde
        self.section = section
        self.subject = sbj

    # method
    def study(self):
        print("I'am studying")
    def print_grade(self):
        print(f"My grade is {self.grade}")


class Waiter(Person):
    # method
    def serve_food(self):
        print("Food is served")
    def check_bill(self):
        print("Bill has been paid")


# talha = Person("Talha", 12, "Male")
# ashir = Person("Ashir", 45, "Male")

# talha.print_name()
# ashir.print_name()


# std_obj = Student("Nasir", 22, "Male")

# std_obj.print_name()
# std_obj.study()

# per_obj = Person("Talha", 22, "Male")
# per_obj.print_name()

# waiter_object = Waiter("Ali", 32, "Male")

# waiter_object.speak()
# waiter_object.serve_food()
# waiter_object.check_bill()
        

std2 = Student("Talha", 22, "Male", "A", "green", "Maths")
std2.print_grade()
std2.speak()
std2.print_name()
std2.study()




# write a parent class Vehicle and it's attributes are model (2021 ya 2015), name (like "civic" ya "cultus"), color andddddddddd methods are run(), horn()

# create a child class Car inheriting attributes and methods of it's parent class which is Vehicle with additional methods drift()


# add additional attributes too like seats (4 ya 7)