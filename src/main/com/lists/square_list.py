#generate and print a list of the first and last 5 elements where the values are square numbers between 1 and 30 (both included).
class Sq_li:
    def square(self):
        l2=[]
        for i in range(1,20):
            x=i**2
            l2.append(x)
        print(l2[:5])
        print(l2[-5:])
    #square()
#program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False.
    def prime(self,l):
        for i in l:
            if i%2 == 0:
                print(i)
                return False
        return True

    #list=[1,3,7,5]
    #print(prime(list))
if __name__ == '__main__':
    obj=Sq_li()
    obj.square()
    list = [1, 3, 7, 5]
    print(obj.prime(list))