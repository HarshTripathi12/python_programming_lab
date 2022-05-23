# The amount to be withdrawn is to be entered by the user.
amount = eval(input('Enter the Rupees : '))
#tt,fh,h=0
tt=amount//2000
amount%=2000
fh=amount//500
amount%=500
h=amount//100
amount%=100
out=f'2000 notes are {tt} 500 notes are {fh} 100 notes are {h}'
print(out)

