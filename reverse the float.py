import numpy as np
lst = list(map(int, input().split()))
out = np.array(lst, dtype = float)
print(out[::-1])
