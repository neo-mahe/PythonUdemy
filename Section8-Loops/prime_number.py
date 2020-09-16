# Prime numbers are numbers that have only 2 factors: 1 and themselves.
# To check if the number entered by the user is prime number or not
import math

num = int(input("Enter any positive number to check if it's a prime number: "))
if num > 1:
    for i in range(1, num):
        print(num % i)
        if (num % i) == 0:
            print(i, num)
            print(num, "is not a prime number")


        else:
            print(num, "is a prime number")
else:
    print(num, "is not a valid input")

help(math.floor)