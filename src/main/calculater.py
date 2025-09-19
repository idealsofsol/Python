class Calculator:  

    def add(self,x:int,y:int):
        return x+y

    def subtract(self,x:int,y:int):
        result = x-y
        print(f"Subtract of {x} and {y} is :", result)

    def multiply(self,x:int,y:int):
       multiply_result=x*y
       print(f"Multiply of {x} and {y} is :", multiply_result)

    def division(self,x:int,y:int):
        if y==0:
            print("Error! division by zero")
        else:    
            division_result = x/y
            print(f"Division of {x} and {y} is :", division_result)
    
    