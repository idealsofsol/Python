from calculater import Calculator
from constructor_practice import Constructor

def print_hi(name:str):
    print(f'Hi, {name}') 

def run_calculator(num1:int,num2:int,choice:str):
    calsi =  Calculator()

    if choice == '1':
        calsi.add(num1,num2)
    elif choice == '2':
        calsi.subtract(num1,num2)
    elif choice == '3':
        calsi.multiply(num1,num2)
    elif choice == '4':
        calsi.division(num1,num2)
    else:
        print("Invalid Input")

def practice_constructor(num1:int,num2:int):
    obj = Constructor(num1,num2)
    obj.add()
    obj1 = Constructor(10,20)
    obj1.add()
if __name__ == '__main__':
    print("Welcome to calculator")
    num1:int = int(input("Enter first number: "))
    num2:int = int(input("Enter second number: ")) 

    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = input("Enter choice (1/2/3/4):")
    #run_calculator(num1,num2,choice)

    practice_constructor(num1,num2)