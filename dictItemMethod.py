a={"Python":101,"Java":202,"Oracle":303,"Django":404}
print(a)
kv=a.items()
for p in kv:
    print(p[0],p[1])
print('Python' in a)
print(20 in a)
b=a.copy()
print(b)
a.pop('Java')
print(a)
a.popitem()
print(a)
a.clear()
print(a)
