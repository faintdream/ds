def removeConsecutiveDuplicates(string):
    if len(string) <= 1 :
        return string
    
    if string[0] == string[1]:
        output = removeConsecutiveDuplicates(string[1:])    
        return ''+ output
    else:
        output = removeConsecutiveDuplicates(string[1:])    
        return string[0]+output
# Main
#string = input().strip()
string = 'xxxyyyzwwzzz'
#string='aabcca'
print(removeConsecutiveDuplicates(string))
