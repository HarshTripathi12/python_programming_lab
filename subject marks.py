marks = {'maths' : 35,'english' : 53,'python' : 23}
out = {}
for i in marks.values():
    out[i] = []
for i in marks.keys():
    x=marks[i]
    out[x].append(i)
print(out)
        
