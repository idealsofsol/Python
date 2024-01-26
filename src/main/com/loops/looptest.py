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

    def reverse_string(self, name):
       # name = "Anjali"
        size = len(name)
        for i in range(size-1, -1, -1):
            print(name[i], end='')


#Write a program to use for loop to print the following reverse number pattern
    def reverse_number_pattern(self):
        row_count=5
        column_count=5
        for i in range(0, row_count+1, 1):
            for j in range(column_count-i, 0, -1):
                print(f'{j}',end=' ')
            print(' ')


#Display numbers from -10 to -1 using for loop
    def reverse_numbers(self):
        i=0
        for i in range(-10,0):
            print(i)


#Use else block to display a message “Done” after successful execution of for loop
    def use_else_block(self):
        for i in range(5):
            print(i)
        else:
            print("Done!")

#Write a program to display all prime numbers within a range
    def prime_numbers(self, n):
        for num in range(0,n+1):
            if num > 0:
                for i in range(2,num):
                    if num%i==0:
                        print('not prime')
                        break

                else:
                    print(num)

#Display Fibonacci series up to 10 terms
    def fibonacci_number(self,number1,number2):
        print("enter the fibonacci number")
        for i in range(10):
            print(number1,end=" ")
            res = number1 + number2

            number1 = number2
            number2 = res

#Find the factorial of a given number
    def factorial_numbers(self,n):
        factorial = 1
        for i in range(n,0,-1):
            factorial = factorial * i
            print(f'factorial is {i}: ',factorial)

#Reverse a given integer number
    def reverse_integer_number(self,n):
        reverse_number = 0
        while n > 0:
            remainder = n % 10
            reverse_number = (reverse_number * 10) + remainder
            n = n // 10
            print("reverse number ",reverse_number)

# Use a loop to display elements from a given list present at odd index positions
    def using_loop_to_display_elements(self,my_list):
        for i in my_list[1:2]:
            print(i, end=" ")

#Calculate the cube of all numbers from 1 to a given number
    def cube(self,n):
        for i in range(1,n):
            cube = i * i * i
            print(f'cube of {i} : {cube}')


#
    def pattern(self):
        row_count = 5
        for i in range(1, row_count + 1, 1):
            for j in range(1, i + 1, 1):
                print('*', end=' ')
            print("")
        row_count = 5
        for i in range(row_count,0, -1):
            for j in range(1, i - 1):
                print('*', end=' ')
            print("")
