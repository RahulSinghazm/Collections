a=[10,20,30,40,50,60]
print(a)
s=0
for p in a:
    s=s+p
    print(s)
    i=0
    s2=0
    while i<len(a):
        s2=s2+a[i]
        i=i+1
print(s2)
