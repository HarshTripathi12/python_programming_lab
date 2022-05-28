def factorial(n):
    fact=1
    if n>0:
        for i in range(1,n+1):
            fact*=i
        return fact
    elif n<0:
        for i in range(-1,n-1,-1):
            fact*=i  
        return fact           
a=int(input("enter a no.: "))    
print(factorial(a))
