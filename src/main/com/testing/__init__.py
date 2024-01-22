from src.main.com.testing import forloop,whileloop

if __name__ == '__main__':
    obj = forloop.Loops()
    obj.numbers(5)
    obj2=forloop.List()
    x=[6,7,8,9,10]
    obj2.iterate(x)
    obj3=forloop.Square()
    obj3.sq()
    obj4=whileloop.While_number()
    obj4.whileloop()
    obj5=whileloop.Sum()
    obj5.sum_num()
