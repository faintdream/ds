def sumArray(arr):    
    if len(arr) == 0:
        return 0
    
    return int(arr[0]+sumArray(arr[1:])) 

    
   
# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
#n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
print(sumArray(arr))
