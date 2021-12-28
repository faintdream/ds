n = int(input())

def fibo(m):
    if m == 1 or m == 2:
        return 1
    return int(fibo(m -1) + fibo(m - 2))
        
print(fibo(n))