def mergeSort(arr):
    if len(arr) <= 1:
        return -1

    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    mergeSort(left)
    mergeSort(right)
    i=j=k=0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k]= right[j]
            j += 1
        k+= 1
    while i < len(left):
        arr[k] = left[i]
        i+= 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
    


# Main
#n=int(input())
#arr=list(int(i) for i in input().strip().split(' '))
arr = [2, 1, 5, 2, 3]

mergeSort(arr)
print(*arr)
