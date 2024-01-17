from src.main.com.lists import (list_basics,
 list_dup, remove_list, square_list, two_lists, concat, add_list, count_list, \
    diff_list, list_arthematic_opratns)
if __name__=='__main__':
    obj = list_basics.Basics()
    obj.li()
    x=[1,2,3,4,5]
    obj.two_lists()
    obj.add(x)

    obj2 = list_dup.List_dup()
    y = [1, 2, 3, 4, 5, 2, 3, 6, ]
    obj2.duplicate(y)
    z = [23, 4, 56, 78, 89, 90]
    obj2.copy(z)
    obj2.empty()
    list = ['sonyaa', 'bravo', '1234', 'aka', 'jimm']
    obj2.longer(list)

    obj3 = remove_list.Remove()
    list1 = ['orange', 'mango', 'ape', 'book', 'pig', 'red']
    obj3.remove(list1)
    obj3.rm_even(list1)
    obj3.rm(list1)

    obj4 = square_list.Sq_li()

    obj4.square()
    list = [1, 3, 7, 5]
    print(obj4.prime(list))

    obj5 = two_lists.Concat()
    l1 = [1, 2, 3, 4, 5]
    l2 = [13, 44, 55, 5]
    obj5.two_list(l1,l2)

    obj6 = concat.Concat()
    obj6.concating('p')

    obj7 = add_list.List_cnvrsns()
    l = ['j', 'a', 'v', 'a']
    obj7.string(l)
    list1 = [1, 2, 3, 4, 5]
    list2 = ['j', 'a', 'v', 'a']
    obj7.lists(list1,list2)

    obj8 = count_list.List_count()
    l = ['aba', 'bab', '121', 'cccc', '456']
    obj8.counting(l)

    obj9 = diff_list.Diff()
    l1 = [2, 4, 6, 8, 10]
    l2 = [1, 3, 5, 7, 19]
    obj9.difference(l1,l2)
    obj9.lis()
    obj9.spec_ind()


    obj10 = list_arthematic_opratns.arithematic()
    l = [2, 3, 4, 5, 6]
    obj10.arith(l)
    obj10.arith2(l)
    obj10.largest(l)
    obj10.smallest(l)
    obj10.sec_small()
    obj10.unique()
    obj10.freq()
    obj10.collectns(l)

