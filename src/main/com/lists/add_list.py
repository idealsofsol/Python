#Convert a list of characters into a string
import random
class List_cnvrsns:
    def __init__(self):
        pass
    def string(self,l):
        s=''.join(l)
        print(s)

    #string(l)
# append a list to the second list.
    def lists(self,l1,l2):
        l3=l1+l2
        print(l3)
        l1.extend(l2)
        print(l1)

    #list1 = [1, 2, 3, 4, 5]
    #list2 = ['j', 'a', 'v', 'a']
    #lists(list1,list2)

    list3=['j','a','v','a']
    print(random.choice(list3))
if __name__ == '__main__':
    obj= List_cnvrsns()
    l = ['j', 'a', 'v', 'a']
    obj.string(l)
    list1 = [1, 2, 3, 4, 5]
    list2 = ['j', 'a', 'v', 'a']
    #list3 = ['j', 'a', 'v', 'a']
    obj.lists(list1,list2)
