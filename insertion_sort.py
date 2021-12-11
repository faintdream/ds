print('Input unsorted list items ', end='')
lst=[ int(x)for x in input().split() ]
j= 0 

for i in range(len(lst)):
    j = i 
    while j > 0:
        if lst[j] < lst[j - 1]:
            lst[j],lst[j-1]=lst[j-1],lst[j]
        j -= 1
print(lst)

