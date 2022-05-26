st = input('Enter your string to check is it palindrome: ')
x=st
if st == st[::-1]:
    print("It is Palindrome")
else:
    print("It is not Palindrome")
