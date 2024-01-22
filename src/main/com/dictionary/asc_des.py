#Write a Python script to sort(ascending and descending) a dictionary by value.


class Sorting:
    def asc(self,d):
        z=sorted(d.items(),key=lambda k: k[1])
        print(z)

    def dec(self,d):
        z=sorted(d.items(),key=lambda item: item[1])
        r=z[::-1]
        print(r)
#Write a Python program to sort a given dictionary by key
    def sort_key(self,d):
        for k in sorted(d):
            print(k,d[k])

if __name__=='__main__':
    obj=Sorting()
    y = {1: 2, 3: 1, 5: 3, 2: 4, 4: 0}
    obj.asc(y)
    obj.dec(y)
    obj.sort_key(y)
