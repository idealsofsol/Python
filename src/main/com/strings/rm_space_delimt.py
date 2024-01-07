import re
stmnt=' hello how are you doing  '
# to match whitespace characters and remove them using the re.sub() function.
stmnt_nospace=re.sub(r'\s+','',stmnt)
print(stmnt_nospace)
stmnt_nospace2=stmnt.strip(' ')
print(stmnt_nospace2)
stmnt2='''this is a long text,

i am doing python,

string split case'''
print(stmnt2)
stmnt3=('this is a long text',

'i am doing python',

'string split case')
print(stmnt3)
lstmnt=stmnt.lstrip()
print(lstmnt)
rstmnt=stmnt.rstrip()
print(rstmnt)
stmnt_lrstrip=stmnt.strip()
print(stmnt_lrstrip)
