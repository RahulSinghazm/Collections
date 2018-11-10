a={"Python":101,"Java":202,"Oracle":303,"Django":404}
print(a)
kv=a.items()
print(kv)
sum=0
for p in kv:
    print(p[0],p[1])
    sum=sum+p[1]
print('Total:',sum)

