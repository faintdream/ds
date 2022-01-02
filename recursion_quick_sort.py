def partition(arr,start,end):
    
    pivot = arr[end]  
    pi = start
    for i in range(start,end):
        if arr[i] <= pivot:
            arr[i],arr[pi]= arr[pi],arr[i]
            pi += 1
    #print('arr[end] ',arr[end],' arr[pi] ',arr[pi])
    arr[pi],arr[end]=arr[end],arr[pi]
    return pi
def quickSort(arr,start,end):
    if start >= end :
        return 
    print(arr)
    pi =partition(arr,start,end)
    quickSort(arr,start, pi-1)
    quickSort(arr,pi+1, end)


#arr=[2, 6, 8, 5, 4, 3]
arr=list(int(i) for i in input().strip().split(' '))
quickSort(arr,0,len(arr)-1)
print(arr)