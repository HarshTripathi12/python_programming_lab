dct = {'name' : 'Harsh', 'Section' : 'H'}
v='H'
for i in dct.copy ():
    if dct[i]==v:
        dct.pop(i)
print (dct)
