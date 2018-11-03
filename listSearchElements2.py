a=[10,20,30,40,50]
print(a)
while True:
    i=int(input('Enter Search element:'))
    p=int(i)
    if p in a:
        print('Element is found')
        break
    else:
        print('Element is not found')
