class LoopsTest:
    # Print First 10 natural numbers using while loop
    def print_natural_numbers(self):
        i = 1
        while i <= 10:
            print(i)
            i += 1  # i=i+1

    # Write a program to print the following number pattern using a loop
    def print_pattern(self):
        row_count = 5
        for i in range(1, row_count + 1, 1):
            for j in range(1, i + 1, 1):
                print(f'{j}', end=' ')
            print("")

    # Calculate the sum of all numbers from 1 to a given number
    def sum_of_given_number(self):
        n = int(input("Enter number "))
        sum = 0
        for i in range(1, n + 1, 1):
            sum = sum + i
            print(f'sum is {i} : ', sum)

    # Write a program to print multiplication table of a given number
    def print_multiplication(self):
        x = 2
        for i in range(11):
            product = x * i
            print(f'product is {i} : ', product)

    # Display numbers from a list using loop
    def list_numbers(self):
        list = eval(input('enter number of list'))
        for i in list:
            if i > 500:
                break
            elif i > 150:
                continue
            elif i % 5 == 0:
                print(i)


# Count the total number of digits in a number
    def total_number_of_digits(self):
        number = int(input("Enter the number "))
        i=1
        while number != 0:
            number = number//10
            print('total digits :',i)
            i += 1


#Print list in reverse order using a loop
    def list_in_reverse(self):
        list=eval(input('Enter list of numbers '))
        size=len(list)-1
        for i in range(size, -1, -1):
            print(list[i])

    def reverse_string(self):
        m="Anjali"[::-1]
        print(m)


#Write a program to use for loop to print the following reverse number pattern
    def reverse_number_pattern(self):
        row_count=5
        column_count=5
        for i in range(0, row_count+1, 1):
            for j in range(column_count-i, 0, -1):
                print(f'{j}',end=' ')
            print(' ')
