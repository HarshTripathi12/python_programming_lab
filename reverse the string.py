st = input('Enter the string')
st = st[::-1]
out = st.split()[::-1]
res = ' '.join(out)
print (res)
