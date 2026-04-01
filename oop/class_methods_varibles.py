class computer:
    category="laptop"
    def __init__(self,ram,storage,processor):
        
        self.ram=ram
        self.storage=storage
        self.processor=processor

    def config(self):
       
        print(f"RAM : {self.ram}")
        print(f"storage : {self.storage}")
        print(f"processor : {self.processor}")

    @classmethod
    def info(cls):
        print(f"category : {cls.category}")
    @staticmethod
    def go_to_bytes(GB):
        print(f"bytes : {GB * (1024 ** 3)}")


com1=computer("16GB","256GB","i7")
com2=computer("24GB","512GB","i9")
print("computer 1 configurations : ")
com1.config()
print("computer 2 configurations : ")
com2.config()
print(com1.category)
computer.info()
computer.go_to_bytes(15)