"""Write the program to create building structure like the burj khaleefa with equivalent binary numbers

Input Format

input for the height(number of lines)

Constraints

0>=height and height<=50"""
n = int(input())
l = len(bin(n))-2

for k in range(n+1):
    k=bin(k)[2:]
    p=len(k)
    print(' '*(l-p)+k)
