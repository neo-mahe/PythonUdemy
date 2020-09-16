# for i in range (1, 11):
#     print(i)
#
# string_example= 'Hey There'
# for ch in string_example:
#     print(ch)

# for i in range(12, 0, -2):
#     print(i)
#

num =5
for i in range(2, 4):
    if num % i == 0:
        print(num % i)
        print(f"it's not a prime number and value of num is {num} and i is {i}")
    else:
        print(f"it's a prime number and the value of num is {num} and i is {i}")
        break

def check_prime(num):
    for i in range(3, num):
        if num % i == 0:
            print(f"Not prime and value of i is {i}")
            break
    else:
        print(f"prime number and value of i is {i}")


def is_prime(number):
    if number < 2:
        return False
    # check if number is divisible by 2 to number -1
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True
