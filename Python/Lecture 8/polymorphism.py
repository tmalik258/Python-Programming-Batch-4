class Vehicle():    # base class
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("move!")

class Car(Vehicle):     # derived class
    pass

class Boat(Vehicle):
    # method overriding
    def move(self):
        print("Sail!")
    
    def move(self):
        print('hello')
    

class Plane(Vehicle):
    # method overriding
    def move(self):
        print("Fly!")


civic = Car("honda", "civic")

titanic = Boat("Titanic", "Elizabeth")

boeing = Plane("Boeing", "747")


civic.move()
titanic.move()
boeing.move()

# overloading
def print_name():
    print("my name is khan")

def print_name(name):
    print(f"my name is {name}")


print_name()
print_name("talha")