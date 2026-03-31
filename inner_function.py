def outer():
    print("this is outer function")
    def inner():
        return "this is inner function" 
        
    return inner

res=outer()
print(res())