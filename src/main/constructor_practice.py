class Constructor:
    x:int
    y:int  
    def __init__(self, x:int,y:int):
        self.x=x
        self.y=y
        print(f'Value of X={x} and Y={y}')

    def add(self):
        result = self.x + self.y
        print(f"Addition of {self.x} and {self.y} is :", result)

    def subtract(self):
        result = self.x - self.y
        print(f"Subtract of {self.x} and {self.y} is :", result)

    def multiply(self):
       result = self.x*self.y
       print(f"Multiply of {self.x} and {self.y} is :", result)

    def division(self):
        if self.y == 0:
            print("Error! division by zero")
        else:    
            division_result = self.x/self.y
            print(f"Division of {self.x} and {self.y} is :", division_result)
    
    