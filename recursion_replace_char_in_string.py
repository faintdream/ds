
def replace_chars(s,a,b):
    if len(s) == 0 :
        return s
    output=replace_chars(s[1:],a,b)
    if s[0] == a:
        return str(b + output )
    else:
        return s[0]+ output

print(replace_chars('my name is anthony', 'a', 'X'))