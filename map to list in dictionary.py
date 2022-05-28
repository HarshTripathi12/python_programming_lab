d={}
name = list(map(str,input().split()))
age = list(map(int,input().split()))
l=len(name)
for i in range(l):
    a=name[i]
    b=age[i]
    d[a]=b

print(d)
