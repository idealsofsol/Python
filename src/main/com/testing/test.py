class Test:
    def natural(self):
        n = 10

        i = 1
        while i < n+1:


            print(i)
            i = i + 1
#Write a program to print the following number pattern using a loop.
    def number(self,n):

        for i in range(1,n+1):
            print(' '.join(map(str, range(1, i + 1))))

#Calculate the sum of all numbers from 1 to a given number
    def sum(self,n):
        s=0
        for i in range(1,n+1):
            s=s+i
        print(s)
#Write a program to print multiplication table of a given number
    def multi(self,n):
        for i in range(1,n+1):
            p=2*i
            print(p)
#Display numbers from a list using loop,The number must be divisible by five,If the number is greater than 150, then skip it and move to the next number
#If the number is greater than 500, then stop the loop
    def list(self):
        x=[112, 75, 150, 180, 145, 525, 50]
        for i in x:
            if i > 500:
                break
            elif i>150:
                continue
            elif i%5==0:
                print(i)
#Write a program to count the total number of digits in a number using a while loop.
    def digits(self,x):
        c=0
        while x!=0:
            x=x//10
            c=c+1
        print(c)
#Write a program to use for loop to print the following reverse number pattern
    def reverse(self):
        for i in range(1,n+1):
            #for j in range(i,-1):
                #print(' '.join(j))
            print(i)
#Print list in reverse order using a loop
    def rev(self):
        list1 = [10, 20, 30, 40, 50]
        list2=reversed(list1)
        for i in list2:
            print(i)
#Display numbers from -10 to -1 using for loop
    def loop(self):
        for i in range(-10,0):
            print(i)
#Use else block to display a message “Done” after successful execution of for loop
    def msg(self,n):
        for i in range(1,n+1):
            if i==5:
                print('Done!')
            else:
                print(i)
#Write a program to display all prime numbers within a range

    #def prime(self,n):
        #for i in range(0, n+1):
           #if i==2:
             #   print(i)
            #elif i==3:
             #   print(i)
            #elif i%2==0 :
             #   print('not prime')
            #elif i%3==0:
             #   print('not prime')
            #else:
                #print(i)

#Display Fibonacci series up to 10 terms
    def fib(self,n):
        n1 = 0
        n2 = 1
        for i in range(1, n):
            r = n1 + n2
            n1 = n2
            n2 = r
            print(r)

#Find the factorial of a given number
    def fact(self,n):
        r=1
        for i in range(1,n+1):
            r=r*i
        print(r)
#reverse a given integer number
    #def int_num(self,x):

     #   y=reversed(x)
      #  print(str(y))
#Use a loop to display elements from a given list present at odd index positions
    def display(self):
        x = [2, 3, 4, 5, 6, 7, 8]
        for i in range(1, len(x), 2):
            print(x[i])
#Calculate the cube of all numbers from 1 to a given number
    def cube(self,x):
        for i in range(1,x+1):
            print(i**3)
#Write a program to calculate the sum of series up to n term. For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690
    #def cal(self,x):
    #    for i
#18: Print the following pattern
if __name__ == '__main__':
    x = Test()
    x.natural()
    x.number(5)
    x.sum(10)
    x.multi(10)
    x.list()
    x.digits(234567)
   # x.reverse(5)
    x.rev()
    x.loop()
    x.msg(5)
    #x.prime(31)
    x.fib(8)
    x.fact(5)
    #x.int_num(2345)
    x.display()
    x.cube(5)


