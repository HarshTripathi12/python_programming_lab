rows= int(input('Enter the rows'))
for i in range (1,rows+1):
    for j in range (i):
        print ('*',end = '')
    for j in range (rows-i):
        print (' ',end = '')
    for j in range (rows-i):
        print (' ',end = '')
    for j in range (i):
        print ('*',end = '')
    print ()
for i in range (1,rows+1):
    for j in range (rows+1-i):
        print ('*',end = '')
    for j in range (i-1):
        print (' ',end = '')
    for j in range (i-1):
        print (' ',end = '')
    for j in range (rows+1-i):
        print ('*',end = '')
    print ()
