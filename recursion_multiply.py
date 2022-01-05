m = int(input())
n = int(input())

def mp(m,n):
    if m == 0 or n == 0:
        return 0
    mp(m,n-1)
    return m*n 


print(mp(m,n))