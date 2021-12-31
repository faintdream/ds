from sys import exit


def show_table(val, limit):
    if val == 0 or limit == 0:
        return -1
    output = show_table(val, limit - 1)
    print(val, 'x', limit, '= ', val * limit)
    return val * limit + output


while True:
    try:
        val = int(input('Print table for  ? '))
        show_table(val, 12)
        next = input('press any key to continue or Q to quit ...')
        if next == 'q' or next == 'Q' :
            break
    except ValueError as e:
        print(e)
    
