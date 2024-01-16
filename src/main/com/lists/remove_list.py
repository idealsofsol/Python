#removing the 0th, 4th and 5th elements.
from random import shuffle
class Remove:
    def remove(self,l:list):
        l2=[]
        for i in range(len(l)):
            if i not in(0,4,5):
                l2.append(l[i])
        print(l2)
#list=['orange','mango','ape','book','pig','red']
#remove(list)
#Python program to print the numbers of a specified list after removing even numbers from it.

    def rm_even(self,l):
        x=[]
        for i in range(len(l)):
            if i%2 !=0:
                x.append(l[i])
        print(x)
    #list=['orange','mango','ape','book','pig','red']
    #rm_even(list)
#Python program to shuffle list
    def rm(self, l):
        #list=['orange','mango','ape','book','pig','red']
        shuffle(l)
        print(l)
if __name__ == '__main__':
    obj=Remove()
    list1 = ['orange', 'mango', 'ape', 'book', 'pig', 'red']
    obj.remove(list1)
    obj.rm_even(list1)
    obj.rm(list1)

