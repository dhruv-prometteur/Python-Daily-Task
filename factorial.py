def fact(num):
    res=1
    for i in range(1,num+1):
        res=res*i
    return res

ans=fact(5)
print(ans)
""" factorial with recursion"""
def factorial(num):
    if num==1:
        return 1
    return num * factorial(num-1)

factorial(5)

    