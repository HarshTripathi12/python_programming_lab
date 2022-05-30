def swapercase (st):
    st1 = ''
    for i in st:
        n= order (i)
        if n>=65 and n<=90:
            y = n+32
            st1 = st1 + chr(y)
        elif n>=97 and n<=122:
            y= n-32
        st1 = st1+chr(y)
    return st1
s= input('Enter the string')
print ('Before',s)
out = swapercase(s)
print ('After',out)
