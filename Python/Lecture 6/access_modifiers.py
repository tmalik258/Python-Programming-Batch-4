"""
In Python, there are no access modifiers like private, protected, or public that are used in languages such as Java or C++. Instead, Python uses conventions to indicate the intended use of a variable or function. Here are the conventions used in Python:
"""

# def public_function():
#     pass
# public_variable = 1

# def _proctected_function():
#     pass
# _proctected_function = 1

class access:
    # Public Variable
    public_variable = 1
    # protected Variable
    _protected_variable = 2
    # Private Variable
    __private_variable = 3

    def public_method(self):
        print("Public Method")
    
    def _protected_method(self):
        print("Protected Method")

    def __private_method(self):
        print("Private Method")
# Test Cases
# Accessing public variables and functions (Methods)
m = access()
print(m.public_variable)
m.public_method()

# Protected 
print(m._protected_variable)
m._protected_method()

# Accessing a private method and variable
print(m._access__private_variable)
m._access__private_method()