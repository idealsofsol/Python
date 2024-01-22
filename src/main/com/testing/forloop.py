#Write a for loop to print numbers from 1 to 5.
class Loops:
    def numbers(self,n):
        for i in range(0,n+1):
            print(i)

#How can you use a for loop to iterate through elements in a list?
class List:
    def iterate(self,x):

        for i in x:
            print(i)


#Create a for loop that prints the square of each number from 1 to 3

class Square:
    def sq(self):
        x=[1,2,3]
        for i in x:
            y=i**2
            print(y)


if __name__ == '__main__':
    x = Loops()
    x.numbers(5)
    y = List()
    a = [1, 2, 3, 4, 5]
    z = y.iterate(a)
    b = Square()
    b.sq()