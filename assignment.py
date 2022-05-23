def fact_sum (lst):
    def fact (n):
        f=1
        for i in range (1,n+1):
            f*=i
            return f
    sum=0
    for i in range(lst):
        sum+=i
lst = list(map(int,input().spirit ))
print (fact_sum(lst))
