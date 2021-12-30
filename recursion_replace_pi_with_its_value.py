def replace_pi(arr):
    if len(arr) == 0:
        return arr
    
    if arr[0] == 'p' and arr[1] == 'i':
        output = replace_pi(arr[2:])
        return '3.14' + output 
    else:
        output=replace_pi(arr[1:])
        return arr[0]+output 


print(replace_pi('pipiiipipipiipiiippi'))