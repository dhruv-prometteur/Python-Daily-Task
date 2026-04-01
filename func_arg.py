

def demo(x,y):
    add=x+y
    return add

add=demo(4,5)
print(add)

def demo1(x,y=9):
    add=x+y
    return add

add=demo1(3)
print(add)

def demo2(x,y):
    add=x+y
    return add
add=demo2(y=9,x=5)
print(add)

def demo3(x,*y):
    add=x
    for i in y:
        add+=i
    return add
add=demo3(45,5,8,9,6,3,5,9)
print(add)

def demo4(name,**info):
    print("name : ",name)
    print("age : ",info["age"])
    print("loc : ",info["loc"])
    print("gender : ",info["gender"])

demo4("dhruv",age=23,loc="bilimora",gender="male")

def demo5(name,*,age,location):
    print("Name : ",name)
    print("age : ",age)
    print("location : ",location)

demo5("Dhruv",age=23,location="Bilimora")