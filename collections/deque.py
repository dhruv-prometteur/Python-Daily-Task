from collections import deque


# ----------------------- deque -----------------------

d=deque([1,2,3])
d.append(4)
d.appendleft(0)
print(d)
d.pop()
print(d)
d.popleft()
print(d)

d.extend([4,5])
print(d)
d.extendleft([0,-1])
print(d)
d.rotate(2)
print(d)
d.clear()
print(d)