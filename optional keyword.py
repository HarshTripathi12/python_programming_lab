def student_info(**kw):
 st = f'''
        Name : {kw.get('name')}
        Roll Number : {kw.get('rolln')}
        Section : {kw.get('sec')}
        CPI : {kw.get('cpi')}'''
 return st
dct = {'Name' : 'Harsh','Section' : 'H'}
out = student_info(**dct)
print (out)
