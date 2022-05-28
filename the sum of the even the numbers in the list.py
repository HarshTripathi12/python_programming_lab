a=input("enter space seprated input: ")
lst=list(map(int,a.split(" ")))
sum=0
for i in range(len(lst)):
    if lst[i]%2==0:
        sum+=lst[i]
print(sum)
