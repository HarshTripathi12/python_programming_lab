n=int(input())
a=int(input())
b="*"
for i in range(1,n+1):
    if i!=a and i!=1:
        print(((b).ljust(i)+(b).rjust(i-1)).center(2*n-1))
    else:
        print(((2*i-1)*b).center(2*n-1))
