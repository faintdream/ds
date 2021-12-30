
def replace_chars(s,a,b):
    if len(s) == 0 :        
        return s
    output=replace_chars(s[1:],a,b)
    if s[0] == a:
        #print(b+output)
        return b + output
    else:
        #print(s[0]+output)
        return s[0]+ output

print(replace_chars('my name is anthony', 'a', 'X'))