def disp (*argu,j=''):
    s= map(str,argu)
    return j.join(s)
out = disp(4,5,6,7,'hi',j='*')
print (out)
