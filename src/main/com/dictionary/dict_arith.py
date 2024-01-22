#Write a Python program to sum all the items in a dictionary.
d={1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
x=sum(d.values())
print(x)
y=1
#Write a Python program to multiply all the items in a dictionary.
for k,v in d.items():
    #y=y*d[k]
    y=y*v
print(y)
#Write a Python program to remove a key from a dictionary.
d={1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
i=int(input('enter a value'))
if i in d:
    d.pop(i)
print(d)
#Write a Python program to get the maximum and minimum values of a dictionary
x=max(d.values())
z=min(d.values())
print('max value is',x)
print('min value is',z)
#Write a Python program to remove duplicates from the dictionary.
d={1: 1, 2: 4, 3: 9, 4: 16, 5: 25,6:25}
x={}
for k,v in d.items():
    if v not in x.values():
        x[k]=v
    print(x)