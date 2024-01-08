#Convert a list of characters into a string
def string(l):
    s=''.join(l)
    print(s)
l=['j','a','v','a']
string(l)
# append a list to the second list.
def lists(l1,l2):
    l3=l1+l2
    print(l3)
    l1.extend(l2)
    print(l1)
list1=[1,2,3,4,5]
list2=['j','a','v','a']
lists(list1,list2)
import random
list2=['j','a','v','a']
print(random.choice(list2))