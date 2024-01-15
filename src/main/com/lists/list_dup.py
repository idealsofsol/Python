#program to remove duplicates from a list.
class list_dup()
    def duplicate(l):
        x=set(l)
        print(x)
    y=[1,2,3,4,5,2,3,6,]
    duplicate(y)
#program to copy from a list.
    def copy(l):
        x=l
        print(x)
    y=[23,4,56,78,89,90]
    copy(y)
#rogram to check if a list is empty or not.
    y=[1,2,3,45,6,6]
    if not y:
        print('list empty')
    else:
        print('list not empty')
#program to find the list of words that are longer than n from a given list of words.
    def longer(l):
        n=3
        l2=[]
        for i in l:
            if len(i) >n+1:
                l2.append(i)
        print(l2)
    list=['sonya','bravo','1234','aka','jimm']
    longer(list)
