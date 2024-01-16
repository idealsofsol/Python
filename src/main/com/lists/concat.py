#program to create a list by concatenating a given list with a range from 1 to n.
#Sample list : ['p', 'q']
#n =5
#Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
class Concat:
    def __init__(self):
        pass
    def concating(self, l:list):
        n = 5
        l2 = []
        for i in range(n):
            for y in l:
                l2.append((y+str(i)))
                #print(f'{y}{i}')
        print(l2)

if __name__ == '__main__':
    obj=Concat()
    Sample_list = ['p', 'q']
    obj.concating(Sample_list)
    #print('concat')








