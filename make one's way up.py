n = int(input())
ls = list(map(int,input().split()))
a = ls[1] - ls[0] 
for i in range(len(ls)):
     if (ls[i+1] - ls[i])>ls[i]:
          print("True")
          break
     else:
          print("False")
          break
