import numpy as np
lst=list(map(int,input().strip().split()))
r,c=lst[0],lst[1]
ar=np.eye(r,c)
print(ar)
