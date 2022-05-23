row = int(input('Enter the rows'))
for i in range (1+row+1):
    for j in range (row-i):
        print (' ',end='')
    for j in range (i):
        print ('*',end='')
    for j in range (i-1):
        print ('*',end='')
    print ()
