#Check if a list contains an element
class Basics:
    def li(self):
        l=[1,'a',2,'b',3]
        if 'a' in l:
            print('True')
        else:
            none
    #li()
#terate over 2+ lists at the same time
    def two_lists(self):
        l2=['a','b','c','d','e']
        l3=[1,2,3,4,5]
        l4=['ss','dd','ff','gg','hh']
        l5=zip(l2,l3,l4)
        for i in l5:
            print(i)
  #  two_lists()
#Python program to sum all the items in a list.
    def add(self,list):
        x=0
        for i in list:
            x = x+i
        print(x)

#add(l3)
if __name__ == '__main__':
    obj=Basics()
    obj.li()
    obj.two_lists()
    l3 = [1, 2, 3, 4, 5]
    obj.add(l3)