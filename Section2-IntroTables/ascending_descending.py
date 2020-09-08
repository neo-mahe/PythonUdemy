print("Print table of 5 using f string \n")
for i in range(1, 11):
    print(f"{5} * {i} = {5*i}")

print("printing table of 5 using format method \n")
for i in range(1,11):
    print("{0} * {1} = {2}".format(5,i,5*i))
print("print numbers from 1-10 in ascending order \n")
for i in range(1, 11):
    print(i)

print("print numbers from 10-1 in descending order \n")

for i in range(10,0, -1):
    print(i)

print("print even numbers from 1-10 in ascending order \n")
for i in range(2, 11, 2):
    print(i)

print("print even numbers from 1-10 in descending order \n")
for i in range(10, 0, -2):
    print(i)


print("print odd number from 1-10 in ascending order \n")
for i in range(1, 10, 2):
    print(i)


print("print odd number from 1-10 in descending order \n")
for i in range(9, 1, -2):
    print(i)