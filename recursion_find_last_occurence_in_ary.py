N = int(input('size of array ? '))
arr = list( int(i) for i in input().split())
s = int(input('searching for ? '))

def findIndex(arr,s):
    if len(arr) == 0 :
        return -1
    output = findIndex(arr[1:],s)
    if output != -1 :
        return output + 1
    else:
        if arr[0] == s:
            return 0
        else:
            return -1
    
    
    
print(findIndex(arr,s))