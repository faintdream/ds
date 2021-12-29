def firstIndex(arr, x,si):
   if len(arr) == 0  or si >= len(arr) :
       return -1
   if arr[si] ==x:
       return si
   else:
       return firstIndex(arr,x,si+1)
      
   

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(firstIndex(arr, x,0))
