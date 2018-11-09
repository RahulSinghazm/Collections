a={"Java":101,"Python":202,"Aws":303,"Devops":404}
print(a)
for k,v in a.items():
    print(k,v)
b={"Java":{"Spring":90,"Struts":80,"Jsf":70},"Python":{"Django":99,"Flash":80,"Bottal":78},"Hadoop":{"Hive":90,"Pig":84,"Sqoop":65}}
print(b)
for i,j in b.items():
    print('_______')
    print(i)
    for a,b in j.items():
        print(a,b)
