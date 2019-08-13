a={"Python":101,"Java":202,"Oracle":303,"Django":404}
print(a)
a['Pyramid']=87
print(a)
print(a['Python'])
print(a.get('Django'))
a.pop('Oracle')
print(a)
a.popitem()
print(a)
k=a.keys()
print(k)

v=a.values()
print(v)
