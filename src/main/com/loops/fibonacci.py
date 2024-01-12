number1 = 0
number2 = 1
print("enter the fibonacci number")
for i in range(10):
    print(number1,end=" ")
    res = number1 + number2

    number1 = number2
    number2 = res