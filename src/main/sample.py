'''count = 0
n=int(input('number of users'))
total=0
while count<n:
    x=int(input('enter a number'))
    #print('enter a number')
    count = count + 1
    total=total+x

avg=total/n
print(avg)'''

total = count = 0
infile = open("input.txt","r")
outfile = open("output.txt","w")
try:
    for l in infile:
        try:
            number = int(l)
            total += number
            count += 1

            current_average = total / count
            outfile.write("%d %f\n" % (count, current_average))
            print("Running Average:", current_average)
        except ValueError:
            break
    print("The final average is %f\n" % (total / count))
finally:
    infile.close()
    outfile.close()
    '''
total = count = 0.0
infile = open("input.txt","r")
for h in infile:
  try:
    number = int(h)
    if number == 0:
      continue
    total += number
    count += 1
  except ValueError:
    break
print("The average is %f\n" % (total/count))
infile.close()


infile = open("input.txt","r")
outfile = open("output2.txt","w")
numbers = []

for l in infile:
  try:
    number = int(l)
    if number < 0:
      continue
    else:
      numbers.append(number)
  except ValueError:
    break

  y=reversed(sorted(numbers))
for number in y:
    outfile.write(str("%d\n" % number))

infile.close()
outfile.close()'''





