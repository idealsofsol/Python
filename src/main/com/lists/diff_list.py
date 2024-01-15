#program to calculate the difference between the two lists
class differentiate()
    def difference(l1,l2):
        l3=[]
        for x in range(len(l1)):
            z=l1[x]-l2[x]
            l3.append(z)
        print(l3)
    list1=[2,4,6,8,10]
    list2=[1,3,5,7,19]
    difference(list1,list2)
#program to access the index of a list.
    l=['aba','bab','121','cccc','456']
    index_values=[]
    for i in range(len(l)):

        index_values.append((i,l[i]))
    print(index_values)
#index of an item in a specified list.
    l=['aba','bab','121','cccc','456']
    l3=l.index('121')
    print(l3)