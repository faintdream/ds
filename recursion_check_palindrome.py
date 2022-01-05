
def palindrome(str,start,stop):
    if len(str) <= 1 or  start >= stop :
        return 'true'
    if str[start] != str[stop]:
        return 'false'
    else:
        return palindrome(str,start+1,stop -1)

str =  input()
print(palindrome(str,0,len(str) -1))



