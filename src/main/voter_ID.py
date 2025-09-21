age=int(input("Enter your age"))
if age>=18:
    print("You are eligible for vote")
else:
    print("You are not eligible for vote")

   
   
num=int(input("Enter a numbers"))
print(f"multiplication of tables of {num}")
for i in range(1,11):
    print(f"{num}*{i}={num*i}")


text=input("Enter the string:")
reversed_text=""
for char in text:
    print(f"char value:{char}")
    reversed_text=char+reversed_text
    print(f"{reversed_text}")
print("Reversed string:",reversed_text)



