num1=int(input('Enter the number'))
num2=num1
s=0
while num>0:
    x=num%10
    s+=x**3
    num1=num1//10
if num2==s:
    print (num2)
