from array import *

arr=array("u","dhruv")
print(arr)

for i in arr:
    print(i)

arr1=array("i",[1,2,5,6,8])
arr2=array(arr1.typecode,(i for i in arr1))

arr2.append(12)
arr1.remove(6)
arr2.insert(1,56)
arr2.pop()
print(arr1)
print(arr2)
arr1.clear()
print(arr1)
