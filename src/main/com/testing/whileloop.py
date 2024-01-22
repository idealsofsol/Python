# Write a while loop to print numbers from 1 to 4.
class While_number:
    def whileloop(self):
        x=[1,2,3,45,5]
        i=0
        while i < len(x):
            print(x[i])
            i=i+1

#2. How do you prevent an infinite loop in a while loop?
#by placing condition like incrementing i
#3. Use a while loop to find the sum of numbers from 1 to 5.
class Sum:
    def sum_num(self):
        n=5
        s=0
        i=0
        while i <n+1:
            s=s+i
            i=i+1
        print(s)
if __name__=='__main__':
    x=while_Number()
    x.whileloop()
    y=Sum()
    y.sum_num()
