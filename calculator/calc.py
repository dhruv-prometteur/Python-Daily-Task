def add(*args):
    result=0
    for num in args:
        result+=num
    return result



def mul(*args):
    result=1
    for num in args:
        result *=num
    return result



def sub(*args):
    if not args:
        return 0
    result=args[0]
    for num in args[1:]:
        result-=num
    return result
   


def div(*args):
    if not args:
        return "please provide any number for division"
    result=args[0]
    for num in args[1:]:
        if num==0:
            return "zero division error"
        result/=num
    return result



if __name__=="__main__":
    print(add(2,3,6,5,9))
    print(mul(2,6,5))
    print(sub(5,8,4))
    print(div(10,5,2))