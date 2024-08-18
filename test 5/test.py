
# Basic subclasses - Adam and Eve

class Human:
    def _init_(self, name):
        self.name = name
class Man(Human):
    def _init_(self,name):
        self.name = name
class Woman(Human):
    def _init_(self, name):
        self.name = name
def God():
    return [Man(), Woman()]

# Classy Extentions

# from preloaded import Animal

# class Cat(Animal):
#     def speak(self):
#         return self.name + " meows."

# Currying functions: multiply all elements in an array

def multiply_all(numbers):
    return lambda number : [i * number for i in numbers]

# Is n divisible by (...)?

def is_divisible(*numbers):
    numbers = list(numbers)
    return True if [True if numbers[0] % i == 0 else False for i in numbers].count(False) == 0 else False