#takes two lists and returns True if they have at least one common member.
class Two_list:
    def two_list(self,l1:list,l2:list):
        for i in l1:
            if i in l2:
                print('true')
            else:
                print('none')
    #l1=[1,2,3,4,5]
    #l2=[13,44,55,66]
    #two_list(l1,l2)
if __name__ == '__main__':
    obj=Two_list()
    l1 = [1, 2, 3, 4, 5]
    l2 = [13, 44, 55, 5]
    obj.two_list(l1,l2)