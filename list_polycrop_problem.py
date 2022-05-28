#method-2
list=list(map(int,input("enter input: ").split(" ")))
ls=[]
for i in range(0,len(list) - 1):
    x=list.count(list[i])
    ls.append(x)
print("minimum pocket required is : ",max(ls)) 
