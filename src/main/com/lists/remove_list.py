#removing the 0th, 4th and 5th elements.
def remove(l:list):
    l2=[]
    for i in range(len(l)):
        if i not in(0,4,5):
            l2.append(l[i])
    print(l2)
list=['orange','mango','ape','book','pig','red']
remove(list)
#Python program to print the numbers of a specified list after removing even numbers from it.
def rm_even(l):
    x=[]
    for i in range(len(l)):
        if i%2 !=0:
            x.append(l[i])
    print(x)
list=['orange','mango','ape','book','pig','red']
rm_even(list)
#Python program to shuffle list
from random import shuffle
list=['orange','mango','ape','book','pig','red']
shuffle(list)
print(list)

