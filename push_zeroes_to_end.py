
print('input array elements ', end='')
lst = [int(x) for x in input().split()]

index = 0 
for i in range(len(lst)):
    if lst[i] != 0:
        lst[index] =lst[i]
        index += 1
while index < len(lst):
    lst[index] = 0
    index += 1
    print(lst)