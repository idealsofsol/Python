#Write a Python program to map two lists into a dictionary.
keys = ['red', 'green', 'blue']
values = ['#FF0000', '#008000', '#0000FF']
di=dict(zip(keys,values))
print(di)
#Write a Python program to combine two dictionary by adding values for common keys.
from collections import Counter

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 400, 'd': 400}
d3 = Counter(d1) + Counter(d2)

print(d3)
#d1 = {'a': 100, 'b': 200, 'c':300}
#d2 = {'a': 300, 'b': 200, 'd':400}
#d3={}
#for i in (d1.items(),d2.items()):
 #   if i in d1.items() and i in d2.items():
  #      d3[i]=d1[i]+d2[i])
   #
##Write a Python program to print all distinct values in a dictionary.
#Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
#Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
d={"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}
y=set()
for dic in d:
    for values in dic.values():
        y.add(values)

print(y)
#Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
Sample data : {'1':['a','b'], '2':['c','d']}
Expected Output:ac ad bc bd