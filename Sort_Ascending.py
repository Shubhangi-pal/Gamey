# Sort Your numbers

from array import *

a = array('i', [])

for i in range(8):
    a.append(int(input("Enter a number")))

print(a)
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

print(a)







