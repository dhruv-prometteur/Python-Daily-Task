from functools import reduce

nums=[1,6,2,8,3,5,7,9,14]

evens=list(filter(lambda n:n%2==0,nums))
print(evens)

doubles=list(map(lambda n:n*2,evens))
print(doubles)

sum =reduce(lambda a,b:a+b,doubles)
print(sum)