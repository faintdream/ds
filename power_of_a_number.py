print('input a number and its power, space separated')
a,b = input().split()
a = int(a)
b = int(b) 
def find_power(a,b):
    if b==0:
        return 1
    return a * find_power(a,b-1)
result=find_power(a,b)
print(result)


