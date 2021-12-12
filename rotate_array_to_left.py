print('input array list ', end='')
lst = [ int(i) for i in input().split() ]
print('rotate from index ', end='')
rotate_index = int(input()) 
tmp_lst=[]
l=0
k=0
for i in range(rotate_index):
    tmp_lst.append(lst[i])

while k < rotate_index:
    for j in range(len(lst) -1 ):
        lst[j] =lst[j+1]
    k += 1

j=0 
for i in range(int(len(lst)-rotate_index), len(lst)): 
    lst[i]=tmp_lst[j]
    j+=1

print(lst)
print(tmp_lst)
