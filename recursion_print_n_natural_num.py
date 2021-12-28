print('numbers to print till where ?')
n = int(input())

def print_num(n):
    if n == 0:
        return 1
    print_num(n - 1)
    print(n)

def print_num_reverse(n):
    if n ==0 :
        return 1
    print(n)
    print_num_reverse(n-1)

print_num(n)
print('lets reverse the game ')
print_num_reverse(n)