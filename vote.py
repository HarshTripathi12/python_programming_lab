def checkeligible(x):
    if x>=18:
        return 'Eligible'
    else:
        return 'Not Eligible'
age = int(input("Enter you age: "))
out = checkeligible(age)
print(out)
