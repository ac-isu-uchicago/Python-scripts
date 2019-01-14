l = [1,2,3,4]

list1 = list() # Create an empty list
list2 = list([22, 31, 61]) # Create a list with elements 22, 31, 61
list3 = list(["tom", "jerry", "spyke"]) # Create a list with strings
list5 = list("python") # Create a list with characters p, y, t, h, o, n

l = [1,2,3,4,5]

l[1]
print(l[1])

l[0]
print(l[0])

list1 = [2,3,4,1,32]
2 in list1
#True

33 not in list1
#True

len(list1)
print(len(list1))
print(max(list1))
print(min(list1))
print(sum(list1))

list = [11,33,44,66,788,1]
list[0:5]

print(list[3])

print(list[2:])

list1 = [11, 33]
list2 = [1,9]
list3 = list1 + list2
print(list3)

list4 = [1,2,3,4]
list5 = list4 * 3
print(list5)

list1 = [11,22,44,16,77,98]
22 in list1
#true

22 not in list1
#False

list = [1,2,3,4,5]

for i in list:
    print(i, end=" ")

list1 = [2,3,4,1,32,4]
list1.append(19)

print(list1)

list1.count(4)
list2 = [99, 54]
list1.extend(list2)
print(list1)

list1.index(4)
#2
list1.insert(1, 25)
print(list1)

list1 = [2,25,3,4,1,32,4,19,99,54]
list1.pop(2)
print(list1.pop(2))

print(list1)
list1.remove(32)
print(list1)

list1.reverse()
print(list1)

list1.sort()
print(list1)

list1 = [x for in range(10)]
print(list1)

list2 = [x+1 for x in range(10)]
print(list2)

list3 = [x for x in ranage(10)]
print(list3)

list4 = [x *2 for x in range(10) if x % 2]
print(list4)










