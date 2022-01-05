def sum(k,start,stop):
    if len(k) == 1 or start >= len(k):
        return True 
    
    output= sum(k,start+1,stop)
    #print(output)
    return int(output)+int(k[start])  
#k = str(input())
k = '1234'
#import pdb; pdb.set_trace()
print(sum(k,0,len(k)-1 )-1)