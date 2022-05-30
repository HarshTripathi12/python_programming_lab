def attendance (rolln,lst = range (30,58)):
    return rolln in lst
rl = int(input('Enter the roll number'))
out = attendance(rl,[36,45,51,54,56])
print ('Absent'if out else 'Present')
