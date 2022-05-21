row = int(input('Enter the rows'))
for i in range (row):
    for j in range (row+row):
        if i==0 or i==row-1 or j==0 or j==(row+row)-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()
