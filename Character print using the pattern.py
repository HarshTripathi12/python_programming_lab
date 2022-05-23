row=int(input('Enter the rows'))
k=65
for i in range (1,row+1):
    k=65
    for j in range (i):
        print (chr(k),end='')
        k+=1
    print ()
