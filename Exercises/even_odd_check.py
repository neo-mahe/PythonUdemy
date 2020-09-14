# # Check if a number is even
# i =13
# if i%2==0:
#     print(f"it's an even number as the reminder of {i} is {i%2}")
# else:
#     print(f"the reminder of {i} is {i%2} so it's an odd number")
#
# # Check if any of the number is even using and logical operator
#
# j = 12
# k = 11
#
# if j%2==0 and k%2==0:
#     print("j and i are even")
# else:
#     print("j and i are not even")
#
# # Check if any of the number is even using or logical operator
#
# j = 12
# k = 11
#
# if j%2==0 or k%2==0:
#     print("one of the values from j and i is even")
# else:
#     print(" both j and i are odd")

# Check if any of the number is even using or logical operator
#
# j = 12
# k = 11
#
# if j%2==0 or k%2==0:
#     print("one of the values from j and i is even")
# else:
#     print(" both j and i are odd")

# Else if statements
# i = 15
# if i == 10:
#     print("value of i is 10")
# elif i == 20:
#     print("Value of i is 20")
# else:
#     print("i is neither 10 nor 20")

# using input from the user and doing an operation like sum, add
num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))
print("\n\n1 - Add")
print("2 - Subtract")
print("3 - Divide")
print("4 - Multiply")
choice = int(input("Choose Operation : "))
print(choice)
if choice == 1:
    result = num1 + num2
elif choice == 2:
    result = num1 - num2
elif choice == 3:
    result = num1 / num2
elif choice == 4:
    result = num1 * num2
else:
    result = "Invalid input"
print(f"the result of the number you have entered is: {result}")
