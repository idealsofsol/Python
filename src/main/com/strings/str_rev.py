word='beach'
print(word[:2])
print(word[-1])
w2=word[::-1]
print(w2)
w3='practise code'
w4=w3[::-1]
print(w4)
w5=w3.split()[::-1]
l=[]
for i in w5:
    l.append(i)
print(' '.join(l))
print(len(w3))

