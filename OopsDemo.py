# self keyword is mandatory for calling variable names into method
# Instance and class variables have whole different purpose
# Constructor name should be __init__
# new keyword is not required when you create objet
class Calculator:
    num = 100 # class variable
    # default contructor
    def __init__(self,a, b):
        self.firstNumber = a
        self.secondNumber = b
        print("I am called automatically when object is created")

    def getData(self):
        print("I am now executing as method in class")

    def summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num

obj = Calculator(2, 3)
print(obj.summation())

obj1 = Calculator(4, 5)
print(obj1.summation())
