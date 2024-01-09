print("enter input number")
a = int(input())
if(a%2 == 0):
    print("a is even")



print("enter student percentage")
percentage = int(input())
if(percentage > 90):
    print("grade is A")
elif(percentage > 75):
    print("grade is B")
elif(percentage > 65):
    print("grade is C")
else:
    print("fail")

print("enter value of a")
a=int(input())
print("enter value of b")
b=int(input())
if(a > b):
    print("big number is a")
elif(b > a):
    print("big number is b")
else:
    print("both are equal")