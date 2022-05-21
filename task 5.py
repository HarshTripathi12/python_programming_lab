import numpy as np 
list1 = []
row,col = map(int,input('Row X column :-').split())
for i in range (0,row):
    list2 = list (map(int,input('Enter').split()))[:col]
    list1.append(list2)
arr=np.array(list1)
print(arr.transpose())
print(arr.flatten())
