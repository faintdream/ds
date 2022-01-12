def contains(substr,str):
    if len(substr) == 0 :
        return True
    if len(str) == 0:
        return False

    if substr[0] == str[0] :
        return contains(substr[1:],str[1:])
        
    elif substr[0] != str[0]:
        return contains(substr,str[1:])
    
str = 'st3h5irteuyarh!'
substr = 'shrey9'

# str = input()
# substr = input()
ans = contains(substr,str)
print(ans)