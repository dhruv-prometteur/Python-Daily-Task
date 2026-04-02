from collections import namedtuple


Point=namedtuple('Point',['x','y'],defaults=[0,0])

p1=Point(10,20)
p2=Point(30,40)


print(p1)
print(p2.x)

print(p1._field_defaults)
print(p1._fields)
p3=p1._replace(x=8)
print(p3)

print(p1._asdict())
