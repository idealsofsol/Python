print("enter value of input1")
input1 = int(input())
print("enter value of input2")
input2 = int(input())
print(f'select the operation {input2} :: sum-->1\n Sub-->2\n Mul-->3\n Div-->4\n')
operation = int(input())


def sub():
    print(f'sub of {input1} and {input2} is :: {input1 - input2}')


if (operation == 1):
    sum()
elif (operation == 2):
    sub()
elif (operation == 3):
    print(f'mul of {input1} and {input2} is :: {input1 * input2}')
elif (operation == 4):
    print(f'div of {input1} and {input2} is :: {input1 % input2}')
else:
    print('not exsisted')


def sum():
    print(f'sum of {input1} and {input2} is :: {input1 + input2}')

