a={"Dhruv","Patel","roman"}
b=[12,3,6]
c=dict(zip(a,b))
print(c)


print(c.get("dhruv","not found"))
o=c.keys()
print(o)
for i in o:
    print(i)
print(c.keys())
print(c.values())
