class Person:

    #constructor
    def __init__(self, name):
        self.name = name #instance variables

        #method that returns a string
    def whoami(self):
        return "You are " + self.name

p1 = Person('Austin')
print(p1. whoami())
print(p1. name)

p1.name = 'Dylan'
print(p1.name)