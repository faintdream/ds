#    ┌┐        ┌┐        ╔╗    
#   ▓▓▓▓       ││        ║║    
#  ▓▓▓▓▓▓      ││        ║║    
# ▓▓▓▓▓▓▓▓     ││        ║║    
#▓▓▓▓▓▓▓▓▓▓    ││        ║║    
#────┴┴────────┴┴────────╨╨────
#──SOURCE────HELPER────TARGET──


def towerofhanoi(n, source, aux, dest): 
    if n > 0:
        towerofhanoi(n-1,source, dest, aux)
        print(' move disk ',source, ' to ', dest )
        towerofhanoi(n -1,aux,dest,source)
        
    else:
        return False

n=int(input())
towerofhanoi(n, 'a','b','c')
