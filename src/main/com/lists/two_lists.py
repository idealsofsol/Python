#takes two lists and returns True if they have at least one common member.
class two_lists():
    def two_list(l1:list,l2:list):
        for i in l1:
            if i in l2:
                print('true')
            else:
                print('none')
    l1=[1,2,3,4,5]
    l2=[13,44,55,66]
    two_list(l1,l2)