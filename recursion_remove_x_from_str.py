def removeX(string): 
    if len(string) == 0 :
        return string
    output= removeX(string[1:])
    if string[0] != 'x':
        return string[0] + output
    else:
        return '' + output


# Main
#string = input()
print(removeX('xaxb'))
