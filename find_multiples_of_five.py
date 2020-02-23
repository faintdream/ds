import sys
import fileinput

new_arr =[]
arr = []
max = 0
index =5
for line in fileinput.input():
    arr = line.split(" ")
    fileinput.close()

for i in arr:
    if max < i:
        max =int(i)

while index < max:
    if (index%5) == 0:
        new_arr.append(index)
    index += 1

if new_arr == []:
    print "none"
else:
    for i in new_arr:
        print i,

