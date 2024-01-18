x = 0
for i in range(1, 11):
    print(i)

n = 5
for i in range(10):
    p = n * i
    print(p)

s = 0
number = int(input("enter the number "))
for i in range(1, number + 1, 1):
    s += i
    print(f'value of i :: {i}')
    print('sum is : ', s)

a = 'Anjali good girl'
for i in a:
    print(i)

x = 0
for i in a:
    print(f'the character present at {x} index: {i}')
    x += 1

list_ids = [2,5,8,9,10]
y=0
for id in list_ids:
    id -=2
    print(id)
    id +=2
    y = id
    print(y)
