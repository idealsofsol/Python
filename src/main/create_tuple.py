#Write a Python program to create a tuple with different data types.
class Create:
    def creating(self):
        x=(1,'tea',25.5,3)
        print(x)
#Write a Python program to create a tuple of numbers and print one item.
    def numbers(self):
        y=1,2,3,4,5

        print(y)
#Unpack a tuple in several variables


        n1,n2,n3,n4,n5=y
        print(n1+n2+n3+n4+n5)
#Add item to tuple
    def add_item(self):
        x=(1,2,3,4,5)
        x=x+(9,)
        print(x)
#Write a Python program to convert a tuple to a string.
    def tup_string(self):
        y=('e','x','a','m','p','l','e')
        s=''.join(y)
        print(s)
#Write a Python program to get the 4th element from the last element of a tuple.
    def element(self):
        x = (1, 2, 3, 4, 5, 6, 7, 8)
        print(x[3])
        print(x[-4])
#Repeated items of a tuple
    def repeated(self):
        x=(1,2,3,4,5,5,6,6,7,7,8,8,8,8,8,88,99,3,3,3)
        print(x.count(3))
#Check whether an element exists within a tuple
    def exist(self):
        x=('a',1,2,'b')
        print('a'in x)
if __name__=='__main__':

    x=Create()
    x.creating()
    x.numbers()
    x.add_item()
    x.tup_string()
    x.element()
    x.repeated()
    x.exist()