for i in range(5):
    for j in reversed(range(5)):
        if j <= i:
            print('*', end='', )
        else:
            print(' ', end='')
    for j in range(5):
        if j < i:
            print('*', end='')    
    print()
print(' ' * 3, '*')
for i in range(2):
    for j in reversed(range(5)):
        if i == j:
            print(' ' * 3, '*', end='')
    print()
print(' '* 2 ,'*'  * 3)   
    




        
    
    