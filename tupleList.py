a=((10,20,30),[40,50,60],(70,80,90))
print(a)
for p in a:
    print(p,type(p))
    a[1][1]=100
    print(a)
