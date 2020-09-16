# program to print the all the letters in a string or numbers, here n can be any variable
numbers = [1, 2, 3, 4, 5]
# for n in numbers:
#     print(n)

name = 'Mahesh Singh'
# for n in name:
#     print(n)
# program to print the index for individual letters of a string or number
for index, n in enumerate (numbers):
    print(f"{n} is at index {index}")

for index, n in enumerate(name):
    print(f'letter {n} is at index {index}')