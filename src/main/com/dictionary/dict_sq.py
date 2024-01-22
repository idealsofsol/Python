#Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
#Sample Dictionary ( n = 5) :
#Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
n=5
d={}
for i in range(1,n+1):
    d[i]=i**2
    d.update(d)
print(d)
#Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included)
# and the values are the square of the keys.
n=15
d={}
for i in range(1,n+1):
    d[i]=i**2
    d.update(d)
print(d)
#Write a Python script to merge two Python dictionaries
d1={1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
d2={6: 'a', 7: 'b', 8: 'c', 9: 'd', 10: 'e'}
d3=d1.copy()
for d in (d1,d2):
    d3.update(d)

print(d3)
# Create a dictionary 'd' with color names as keys and corresponding numerical values as values.
d = {'Red': 1, 'Green': 2, 'Blue': 3}
for k,v in d.items():
    print(k, 'crspnds to', d[k])