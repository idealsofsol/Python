from itertools import product
a = {'1': ['a', 'b'], '2': ['c', 'd']}
r=list(product(*a.values()))
print(r)
for i in r:
    x=''.join(i)
    print(x)



