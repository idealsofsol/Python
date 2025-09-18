class calculaotr:
    def __init__(self):
        print("Calculator is ready!")
        
    def add(self,x:int,y:int):
        return x+y
    
    def substract(self,x:int,y:int):
        return x-y
    
    def multiply(self,x:int,y:int):
        return x*y
    
    def divide(self,x:int,y:int):
       if y ==0:
        return"Error! Division by zero is not allowed" 
        return x/y 

        calc=calculator()

    print("Welcome to calculator")


print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Divide")
choice = input("Enter choice (1/2/3/4): ")

num1:int = int(input("Enter first number: "))
num2:int = int(input("Enter second number: ")) 

if choice == '1':
    print("Result:",calculaotr class.add(num1, num2))
elif choice == '2':
    print("Result:",calculaotr class.subtract(num1, num2))
elif choice == '3':
    print("Result:",calculaotr class.multiply(num1, num2))
elif choice == '4':
    print("Result:",calculaotr class.divide(num1, num2))
else:
    print("Invalid Input")

