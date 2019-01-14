#def myfunc()
#     pass

def sum(start, end):
    result = 0
    for i in range(start, end + 1):
        result += i
    print(result)

sum(10, 50)

def sum(start, end):
    result = 0
    for i in range(start, end + 1):
        result += i
    return result

s = sum(10, 50)
print(s)

def sum(start, end):
    if(start > end):
        print("start should be less than end")
        return
    result = 0
    for i in range(start, end + 1):
        result += i
    return result

s = sum(110, 50)
print(s)
def test():
    i = 100
print(test())

global_var = 12  # a global variable


def func():
    local_var = 100  # this is local variable
    print(global_var)  # you can access global variables in side function


func()  # calling function func()

# print(local_var)

xy = 100

def cool():
    xy = 200
    print(xy)

cool()

print(xy)

t = 1

def increment():
    global t #now t insidde the function is s
    t = t + 1
    print(t)

increment()
print(t) #displays 2


t = 1
def increment():
    global t
    t = 100
    t = t + 1
    print(t)

increment()
print(t)

def my_func(a, b, c):
    print(a, b, c)

# using positional arguments only
my_func(12, 13, 14)

# here first argument is passed as positional arguments while other two as keyword argument
my_func(12, b=13, c=14)

# same as above
my_func(12, c=13, b=14)

# this is wrong as positional argument must appear before any keyword argument
# my_func(12, b=13, 14)

def bigger(a, b):
    if a > b:
        return a, b
    else:
        return b, a
s = bigger(12, 100)
print(s)
print(type(s))



