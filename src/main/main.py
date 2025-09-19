from calculater import Calculator


def print_hi(name:str):
    print(f'Hi, {name}') 

def run_calculator():
    print("Welcome to calculator")
    num1:int = int(input("Enter first number: "))
    num2:int = int(input("Enter second number: ")) 

    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = input("Enter choice (1/2/3/4):")

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


if __name__ == '__main__':
    print_hi('Im from main file')
    run_calculator()