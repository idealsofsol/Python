stmnt='areyou3yearsold'
print(stmnt.isalnum())
print(stmnt.isprintable())
stmnt2='32'
print(stmnt2.isalnum())
stmnt3='areyou 3 year sold'
print(stmnt3.isalnum())
print(stmnt3.startswith('areyou'))
stmnt4='@3years#'
print(stmnt4.isalnum())