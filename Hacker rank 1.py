"""Given an space separated sequence of integers, calculate the ratios of its elements that are positive, negative, and zero.

Display the decimal value of each fraction on a new line with 6 places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to 10^-4 are acceptable.
Example arr = [1, 1, 0, -1, -1]

There are n=5 elements, two positive, two negative and one zero. 
Their ratios are 2/5, 2/5 and 1/5. Results are printed as:
0.400000
0.400000
0.200000
So, Write a program to print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with 6 digits after the decimal."""
N = int(input())
listahan = input().split()
diks = {"pos": 0, "neg": 0, "zer": 0}
for i in listahan:
    if int(i) > 0:
        diks["pos"] += 1
    elif int(i) < 0:
        diks["neg"] += 1
    else:
        diks["zer"] += 1     
print(format(diks["pos"]/N, '.6f'))
print(format(diks["neg"]/N, '.6f'))
print(format(diks["zer"]/N, '.6f'))
