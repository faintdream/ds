print('input array 1 ' , end ='')
ar1 = [ int(x) for x in input().split()]
print('input array 2 ' , end ='')
ar2 = [ int(x) for x in input().split()]
i = 0
j = 0
new_ar=[]
while i < len(ar1) and j < len(ar2):
    if ar1[i] < ar2[j]:
        new_ar.append(ar1[i])
        i += 1
    else:
        new_ar.append(ar2[j])
        j +=1
 
while i < len(ar1):
    new_ar.append(ar1[i])
    i += 1
while j < len(ar2):
    new_ar.append(ar2[j])
    j += 1

print('merged array ', new_ar)