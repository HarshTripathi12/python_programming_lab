'''HP:(Hewlett-Packard) is a leading American multinational computer system manufacturer in the world.

The company Hewlett-Packard doesn't like integers that are divisible by 3 or end with the digit 3 in their decimal representation. Integers that meet both conditions are disliked by Hewlett-Packard, too.

Hewlett-Packard starts to write out the positive (greater than 0) integers which he likes: 1,2,4,5,7,8,10,11,14,16,….

Write a program to print the output k-th element of this sequence (the elements are numbered from 1), where user will just enter the position only.

Input Format

The first line contains one integer value of k(1<=k<=1000)

Constraints

(1<=k<=1000)

Output Format

the k-th element of the sequence that was written out by Hewlett-Packard'''
k=int(input())
i=0
ls =[]
for i in range (1001):
    if i%3!=0 and i%10:
        ls.append(i)
print (ls[k-1])
        
