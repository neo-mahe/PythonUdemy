def print_hello_word_twice():
    print("Hello World")
    print("Hello World")


def print_hello_word(no_of_times):
    for i in range(1, no_of_times):
        print("hello world")


def printNumbers(n):
    for i in range(1, n + 1):
        print(i)


def print_squares_of_numbers(n):
    for i in range(1, n + 1):
        print(i * i)


def print_string(str, no_of_times):
    for i in range(1, no_of_times + 1):
        print(str)


# def print_default_values(str="Hey There!!", no_of_times=3):
#     for i in range(1, no_of_times + 1):
#         print(str)

def print_default_values(str="Hey There!!", no_of_times=3):
    for i in range(1, no_of_times + 1):
        print(str)


def print_table(table, start, end):
    for i in range(start, end + 1):
        print(f"{table} * {i} = {table * i}")


print_table(6, 2, 8)
