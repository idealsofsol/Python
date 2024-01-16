#program to remove duplicates from a list.
class List_dup:
    def duplicate(self,l):
        x=set(l)
        print(x)
    #y=[1,2,3,4,5,2,3,6,]
    #duplicate(y)
#program to copy from a list.
    def copy(self,l):
        x=l
        print(x)
   # z=[23,4,56,78,89,90]
    #copy(z)
#rogram to check if a list is empty or not.
    def empty(self):
        y=[1,2,3,45,6,6]
        if not y:
            print('list empty')
        else:
            print('list not empty')
#program to find the list of words that are longer than n from a given list of words.
    def longer(self,l):
        n=3
        l2=[]
        for i in l:
            if len(i) >n+1:
                l2.append(i)
        print(l2)
    #list=['sonyaa','bravo','1234','aka','jimm']
    #longer(list)
if __name__ == '__main__':
    obj=List_dup()
    y = [1, 2, 3, 4, 5, 2, 3, 6, ]
    obj.duplicate(y)
    z = [23, 4, 56, 78, 89, 90]
    obj.copy(z)
    obj.empty()
    list = ['sonyaa', 'bravo', '1234', 'aka', 'jimm']
    obj.longer(list)
