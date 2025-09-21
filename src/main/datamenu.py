print("Welcome to daba\nMENU:")

print("1.Main course\n2.Starters\n3.Deserts\n4.Juice")
choice = int(input("Enter choice (1/2/3/4):"))
print(choice)

match choice:
 case 1:
    print("(a)Biryani\n(b)Fried rice\n(c)Mutton biryani\n(d)Rooti")
    choice1 = input("Enter choice(a/b/c/d):")
    if choice1 not in ['a', 'b', 'c', 'd']:
        print("Invalid choice ❌")
    else:
        print("Valid choice ✅")  
 case 2: 
    print("(a)Dragon chicken\n(b)Chilly chicken\n(c)Chicken popcorn\n(d)Wings")
    choice2 = input("Enter choice(a/b/c/d):")
    if choice2 not in ['a', 'b', 'c', 'd']:
        print("Invalid choice ❌")
    else:
        print("Valid choice ✅")     
 case 3:
    print("(a)Choclate lava cake\n(b)Sizziling brownie\n(c)Ice cream cake")
    choice3 = input("Enter choice(a/b/c/):")
    if choice3 not in ['a', 'b', 'c']:
        print("Invalid choice ❌")
    else:
        print("Valid choice ✅")  
 case 4:
    print("(a)Blue sea\n(b)Mango pinch\n(c)Strawberry")  
    choice4 = input("Enter choice(a/b/c):")
    if choice4 not in ['a', 'b', 'c']:
        print("Invalid choice ❌")
    else:
        print("Valid choice ✅")   
 case _:
       print("wrong choice")                   