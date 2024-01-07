#onvert all lowercase letters to uppercase letters and vice versa.
w1='www.HackerRANK.com'
w2=w1.swapcase()
print(w2)
print(w1[5])##gives alphanet inthat position
#Split the string on a " " (space) delimiter and join using a - hyphen.
w1='hello how are you'
w2=w1.split( )
w3='-'.join(w2)
print(w3)
#given the firstname and lastname of a person on two different lines. Your task is to read and print them:
f_name='vyshnavi'
l_name='kothakota'
stmnt='how are you'
full_stmnt=f_name+' '+l_name+' '+stmnt
print(full_stmnt)
#Given an integer, , print the following values for each integer  from  to :Decimal,Octal,Hexadecimal (capitalized),Binary
from decimal import *
n=15
for i in range(0,n+1):
    D=Decimal(i)
    O=oct(i)[2:]
    H=hex(i)[2:].upper()
    B=bin(i)[2:]
    print(str(D).rjust(3),O.rjust(3),H.rjust(3),B.rjust(3))
#ensure that the first and last names of people begin with a capital letter in their passports.
f_name='vyshnavi'
l_name='kothakota'
full_name=f_name+' '+l_name
print(full_name.title())