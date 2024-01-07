city='newyork'
print(type(city))
city=str("newyork")
print(type(city))
city2='newjersy'
city3=str(city+city2)
print(city3)
city3=str(city+' '+city2)
print(city3)
print(len(city2))
city4=city3.replace('newjersy','newark')
print(city4)
##to count space or to count no of times a letter is occured in word
print(city4.count('n'))
