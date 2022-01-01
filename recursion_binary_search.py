def binary_search(arr,left,right,mid,search):
    if len(arr) == 0 or mid > right or mid < 0:
        return -1
    
    if arr[mid] == search:
        return mid
    elif search < arr[mid]:
        return binary_search(arr,left,right,mid-1,search)    
    else:
        return binary_search(arr,left,right,mid+1,search)
    
arr= [1,2,3,4,5,6,7,8,9]
search =9
print(binary_search(arr,0,len(arr),int(0+len(arr)//2),search))
