'''
name = 'abcd'
reverse_name = ''
lent=len(name)-1
while lent > -1:
    reverse_name = reverse_name+name[lent]
    lent=lent-1
print(reverse_name)

name = 'abcd'
reverse_name = ''
lent=len(name)
index=0
while index < lent:
    reverse_name = name[index]+reverse_name
    index=index+1
print(reverse_name)


def reverse_name(self):
    name = 'abcd'
    rev_strng = ''
    rev1 = ''
    size = len(name)-1
    # print(size)
    for i in range(size, -1, 1):
        rev_strng = rev_strng + (name[i])
    print(rev_strng)
    for c in name:
        rev1 = c + rev1
    print(rev1)'''



for i in range(0,11,2):
    print(i)