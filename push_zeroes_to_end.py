
print('input array elements ', end='')
lst = [int(x) for x in input().split()]

i = 0
j = 0
while i < len(lst):
    if lst[i] == 0:
        j = 0 
        while j < i:
            lst[i],lst[j]=lst[j],lst[i]
            j += 1
    i += 1
    print(lst)
