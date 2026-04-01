class Demo:
    def show(self):
        print("hello this is show method")
    def testing(self):
        print("this is testying method")

obj1=Demo()
obj2=Demo()

obj1.show()
obj2.show()


class computer:
    def __init__(self,name,ram,storage,processor):
        self.name=name
        self.ram=ram
        self.storage=storage
        self.processor=processor

    def config(self):
        print(f"name : {self.name}")
        print(f"ram : {self.ram}")
        print(f"storage : {self.storage}")
        print(f"processor : {self.processor}")


com1=computer("Dell","16GB","256GB","i7")
com2=computer("HP","24GB","512GB","i9")
print("computer 1 configurations : ")
com1.config()
print("computer 2 configurations : ")
com2.config()


class Abc:
    
    def __new__(cls):
        print("constructor called")
        return super(Abc,cls).__new__(cls)
    def __init__(self):
        print("init called")

    def show(self):
        print("hello this is show method")

    def testing(self):
        print("this is testying method")


obj=Abc.__new__(Abc)
obj.show()



