class Create:
# Write a Python program to create a set.
    def data_type(self):
        x=set([1,2,3,4,5])
        print(type(x))
#Write a Python program to iterate over sets.
    def iterate(self):
        x=set([6,7,8,9,10,11,12])
        for i in x:
            print(i)
#. Write a Python program to add member(s) to a set.
    def set_num(self):
        x=set([1,2,3,4,5])
        x.update([9])
        print(x)
#Write a Python program to remove item(s) from a given set.
        x.remove(5)
        print(x)
#Write a Python program to create an intersection of sets.
    def intersection(self):
        a=set(['apple','banana'])
        b=set(['apple','cat'])
        c=a&b
        print(c)
#Write a Python program to create an union of sets.
        c=a.union(b)
        print(c)
#Write a Python program to create set difference.
    def set_difference(self):
        x=set([1,2,3,4])
        y=set([3,4,5,6,7])
        z=y.difference(x)
        print(z)
#Write a Python program to remove all elements from a given set.
    def removal(self):
        e=set([1,2,3,4])
        e.clear()
        print(e)
#Write a Python program to find the maximum and minimum values in a set.
    def max_min(self):
        e=set([1,2,3,4])
        print(max(e))
        print(min(e))
#Write a Python program to find the length of a set.
        print(len(e))
#Write a Python program to check if a given value is present in a set or not.
        print(3 in e)
if __name__=='__main__':
    x=Create()
    x.data_type()
    x.iterate()
    x.set_num()
    x.intersection()
    x.set_difference()
    x.removal()
    x.max_min()