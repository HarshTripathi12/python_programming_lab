n=int(input("enter length of string: "))
lst=[]
list=[]
for i in range(0,n):
    lst.append(int(input("enter value: ")))
for i in lst:
    if i%2==0:
        list.append(i)
print("result",list)        
