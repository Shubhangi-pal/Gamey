# Sort Your numbers

from array import *

a = array('i', [])
length = int(input("Enter how many numbers you want to sort:"))
for i in range(length):
    a.append(int(input("Enter a number")))

print("The list of numbers you have entered : ", a)
count = 0
while count < len(a) -1:
    t = 0
    while t < len(a)- 1:

        if a[t] > a[t+1] :
            a[t], a[t+1] = a[t+1], a[t]

        else :
            pass
        t +=1
    count += 1

print("Your list sorted in ascending order : ", a)







