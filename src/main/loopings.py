correct_pin = "5647"
pin = input("Enter the ATM PIN:")
while pin  != correct_pin:
    print("incorrect PIN try again")
    pin = input("Enter the ATM PIN:")
print("correct PIN")


num = int(input("Enter the number:"))
rev= 0
while num>0:
 digit=num % 10;
 rev = rev*10+digit
 num = num // 10

 print("reversed_number",rev)




 