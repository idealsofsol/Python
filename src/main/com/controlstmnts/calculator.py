print("enter value of input1")
input1=int(input())
print("enter value of input2")
input2=int(input())
print("select the operation:: sum-->1\n Sub-->2\n Mul-->3\n Div-->4\n")
operation=int(input())
if(operation==1):
    print(f'sum of {input1} and {input2} is :: {input1+input2}')
elif(operation == 2):
    print(f'sub of {input1} and {input2} is :: {input1-input2}')
elif(operation == 3):
    print(f'mul of {input1} and {input2} is :: {input1*input2}')
elif(operation == 4):
    print(f'div of {input1} and {input2} is :: {input1%input2}')
else:
    print('not exsisted')