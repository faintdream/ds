def find_sum(k):
    if k == 0 :
        return 1
    elif k < 0:
        return 0
    else:
        #print(find_sum(k -1)+ find_sum(k-2)+ find_sum(k-3))
        return find_sum(k -1)+ find_sum(k-2)+ find_sum(k-3)  

    
     

k = 5
print(find_sum(k))
