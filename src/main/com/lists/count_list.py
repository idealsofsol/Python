#Write a Python program to count no: of strings in list of strings.str leng is 2 or more and the first and
#last characters are the same.
class List_count:
    def counting(self,list):
        c=0
        for i in list:
            print(i)
            if i[0] == i[-1]:
                c=c+1
        print(c)

    #l=['aba','bab','121','cccc','456']
    #counting(l)
#Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
    def sortng(self,n):
        return(n[-1])
    def sort_list(self,tuple):
        return sorted(tuple,key=sortng)


    Sample_List = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    print(sortng(Sample_List))

if __name__ == '__main__':
    obj=List_count()
    l = ['aba', 'bab', '121', 'cccc', '456']
    obj.counting(l)
