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

a =input("enter any string ")
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



s = 'Hello welcome to python'
for i in range(10):
    print(s)

for n in range(21):
   if(n%2 != 0):
       print(n)



for i in range(10,20,+2):
    print(i)


list = eval(input("enter list of numbers: "))
sum = 0
for i in list:
    sum = sum + i
    print("the sum of i : ", sum)

