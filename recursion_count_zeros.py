def count_z(k):
    if k == 0 :
        return 0
    output= count_z(k//10)
    if k%10 == 0 :
        return output+1
    else:
        return output

k = int(input())
if k == 0:
    print(1)
else:
	print(count_z(k))