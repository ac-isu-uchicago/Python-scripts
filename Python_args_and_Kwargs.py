#def sum(a, b):
    #print("sum is", a+b)

def sum(*args):
    s = 0
    for i in args:
        s += i
    print("sum is", s)


sum(1,2,3)

sum(1,2,3,4,5,7)

sum(1,2,3,4,5,7,8,9,10)


def my_func(**kwargs):
    for i, j in kwargs.items():
        print(i, j)


my_func(name='tim', sport='football', roll=19)


def my_three(a, b, c):
    print(a, b, c)


a = [1, 2, 3]
my_three(*a)  # here list is broken into three elements


