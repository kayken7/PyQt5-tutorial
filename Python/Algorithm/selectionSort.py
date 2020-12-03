import random

list1 = []

while len(list1) != 10:
    newNumber = random.randint(1, 10)
    if newNumber not in list1:
        list1.append(newNumber)

print("*Before selection sort: ")
print(list1)
count = len(list1)

for i in range(0, count-1):
    minIndex = i
    for j in range(i+1, count):
        print(i,j)
        if list1[j] < list1[minIndex]:
            minIndex = j
    temp = list1[i]
    list1[i] = list1[minIndex]
    list1[minIndex] = temp

print("*After selection sort: ")
print(list1)
