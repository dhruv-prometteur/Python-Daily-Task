def square(num):
    return num * num
def cube(num):
    return num * num * num

# def operate(num,operation):
#     return operation(num)

def operate(nums,operation):
    for i in nums:
        print(operation(i))

ans=operate([7,3,4],cube)
operate([4,5,8],cube)
print(ans)
