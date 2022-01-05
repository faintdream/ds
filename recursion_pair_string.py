def pair_star(k):
    if len(k) <= 1:
        return k
    
    
    # print('output ', output)
    if k[0] == k[1]:
        output= pair_star(k[2:])
        return   k[1]+'*'+output 
    else:
        output= pair_star(k[1:])
        return k[0]+ output
# k = input()
k ='abbacccbaaabcjjhhhhfkkdsddff'
print(pair_star(k))