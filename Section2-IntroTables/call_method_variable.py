name = None


def calling_name1():
    global name
    name = "Jenny"
    print(name)


calling_name1()


def calling_jacob():
    print(name)


calling_jacob()


# a = 10
a = None

def something():
    global a
    a = 15
    print("in fun ", a)


something()
print("outside ", a)


def saySomething():
    print(a)


#
saySomething()
print("outside ", a)
