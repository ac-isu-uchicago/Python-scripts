class A():

    def __init__(self):
        self.__x = 1

    def m1(self):
        print("m1 from A")


class B(A):

    def __init__(self):
        self.__y = 1

    def m1(self):
        print("m1 from B")


c = B()
c.m1()