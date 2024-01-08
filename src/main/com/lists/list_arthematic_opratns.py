#Python program to multiply all the items in a list.
def arith(list):
    x=1
    for i in list:
        x=x*i
    print(x)
l=[2,3,4,5,6]
arith(l)
#Python program to add all the items in a list.
def arith(list):
    x=1
    for i in list:
        x=x+i
    print(x)
l=[2,3,4,5,6]
arith(l)
#Write a Python program to get the largest number from a list.
def largest(list):
    list.sort()
    print(list[-1])
l=[10,12,14,25,34,16,7,3,2]
largest(l)
#Write a Python program to get the largest number from a list.
def smallest(list):
    list.sort()
    print(list[0])
l = [10, 12, 14, 25, 34, 16, 7, 3, 2]
smallest(l)
#program to find the second smallest ,largest number in a list.
l = [10, 12, 14, 25, 34, 16, 7, 3, 2]
l.sort()
print('sec smallest is', l[1])
print('sec largest is', l[-2])
# program to get unique values from a list.
l = [10, 12, 14,2,3,25, 25, 34, 16, 7, 3, 2]
l2=set(l)
print(l2)
#program to get the frequency of elements in a list.
l = [10, 12, 12,14,2,3,25, 25,25, 34, 16, 7, 3, 2]

y=[]
for i in set(l):
    count=l.count(i)
    y.append((i,count))
print(y)
import collections
y=collections.Counter(l)
print(y)