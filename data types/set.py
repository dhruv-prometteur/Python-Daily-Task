set={1,2,3,4,5,6,6,7}
print(set)
print(4 in set)

set.add(34)
set.pop()
set.remove(3)
set.discard(7)
print(set)

s1={1,2,3,4,5}
s2={1.3,4,7,8,9}

print(s1-s2)
print(s1.union(s2))
print(s1.intersection(s2))
print(s1 & s2)
print(s1 | s2)
print(s1 ^ s2)