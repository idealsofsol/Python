#rite a Python script to add a key to a dictionary.
#Sample Dictionary : {0: 10, 1: 20}
#Expected Result : {0: 10, 1: 20, 2: 30}

class Adding:
    def add(self):
        d={0:10,1:20}
        #d[3]=30
        d.update({2:30})
        print(d)
#Write a Python script to concatenate the following dictionaries to create a new one.

#dic1={1:10, 2:20},dic2={3:30, 4:40},dic3={5:50,6:60},Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
class Append:
    def join(self):
        dict1={1:10, 2:20}
        dict2={3:30, 4:40}
        dict3={5:50,6:60}
        dict4={}

        for d in (dict1,dict2,dict3):
            dict4.update(d)
        print(dict4)
#Write a Python script to check whether a given key already exists in a dictionary.
class Exist():
    def dict(self):
       d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
       i = int(input('enter a number: '))
       if i in d:
           print('item exist')
       else:
           print('item do not exist')

#Write a Python program to iterate over dictionaries using for loops.
class Ietrate:
    def dict1(self):
        d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
        for d_k,d_v in d.items():
            print(d_k,'->',d_v)





if __name__=='__main__':
    obj=Adding()
    obj.add()
    obj2=Append()
    obj2.join()
    obj3=Exist()
    obj3.dict()
    obj4=Ietrate()
    obj4.dict1()