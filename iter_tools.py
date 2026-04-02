from itertools import product,permutations,combinations,combinations_with_replacement,accumulate


a=[1,2,3,4]
b=[3,4]
#-----------------------product---------------------
# prod1=product(a,b)
# print(list(prod1))
# prod2=product(a,b,repeat=2)
# print(list(prod2))


#-----------------------permutations---------------------
# permutation=permutations(a)
# print(list(permutation))


#-----------------------combination and combination with replacement---------------------
# comb=combinations(a,2)
# print(list(comb))

# comb_wr=combinations_with_replacement(a,2)
# print(list(comb_wr))

#-----------------------accumulate---------------------
# acc=accumulate(a)
# print(list(acc))

from itertools import groupby,count,repeat,cycle,filterfalse

# l=[1,1,2,2,3,4,4,7,5,5,1,2,2]

# for k,g in groupby(l):
#     print(k,list(g))


#--------------------count-----------------
for i in count(10):
    if i>15:
        break
    print(i)
#--------------------repeat-----------------
for x in repeat("A",5):
    print(x)

#--------------------cycle-----------------
data=["red","yellow","blue"]

for i,color in zip(range(6) ,cycle(data)):
    print(color)



#--------------------filterflase-----------------
print(list(filterfalse(lambda x:x%2==0,[1,2,3,4])))