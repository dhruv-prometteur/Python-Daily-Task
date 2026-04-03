import copy
#---------------------------shallow copy---------------------------
l1=[1,2,3,[7,6]]
l2=copy.copy(l1)
l1[3].append(9)
l1.append(8)
l2.append(5)
print(l1)
print(l2)



#--------------------------Deep copy ----------------------------------
l3=[4,5,6,8,[2,3]]
l4=copy.deepcopy(l3)
l3[4].append(1)
l4.append(9)
print(l3)
print(l4)

