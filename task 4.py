import numpy as np 
r,c = map(int,input('Row X column :-').split())
lst1 = list (map(int,input('Element M1 ').split()))
lst2 = list (map(int,input('Element M2 ').split()))
M1 = np.array(lst1).reshape(r,c)
M2 = np.array(lst2).reshape(r,c)
out1 = np.add(M1,M2)
out2 = np.subtract(M1,M2)
out3 = np.divide(M1,M2)
out4 = np.multiply(M1,M2)
out5 = np.power(M1,M2)
print(out1)
print(out2)
print(out3)
print(out4)
print(out5)
