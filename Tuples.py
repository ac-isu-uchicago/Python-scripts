t1 = ()  # creates an empty tuple with no data

t2 = (11, 22, 33)

t3 = tuple([1, 2, 3, 4, 4])  # tuple from array

t4 = tuple("abc")  # tuple from string

t1 = (1,12,55,12,81)
min(t1)
max(t1)
sum(t1)
len(t1)

t = (11,22,33,44,55)
for i in t:
    point(i, end=" ")

t = (11,22,33,44,55)
t[0:2]

t = (11,22,33,44,55)
22 in t
#true
22 not in t
#False
