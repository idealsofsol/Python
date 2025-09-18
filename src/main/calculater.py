class Calculator:  

    def add(self,x:int,y:int):
        return x+y

    def subtract(self,x:int,y:int):
        return x-y

    def multiply(self,x:int,y:int):
        return x*y

    def divide(self,x:int,y:int):
        if y==0:
            return "Error! division by zero"
        return x/y

print("Welcome to calculator")
num1:int = int(input("Enter first number: "))
num2:int = int(input("Enter second number: ")) 

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Divide")
choice = input("Enter choice (1/2/3/4): ")
calsi=new calculator()
if choice == '1':
    add_result=add(num1,num2)
    print("Result:", cal.add_result)
elif choice == '2':
    print("Result:", cal.subtract(num1, num2))
elif choice == '3':
    print("Result:", cal.multiply(num1, num2))
elif choice == '4':
    print("Result:", cal.divide(num1, num2))
else:
    print("Invalid Input")
