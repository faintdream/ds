print('input your array list')
arr = list( int(i) for i in input().split())

def isSorted(arr,si):
    l = len(arr)
    if si == l or si == l -1:
        return True
    if arr[si] > arr[si + 1]:
        return False
    return isSorted(arr,si+1)

print(isSorted(arr,0))
