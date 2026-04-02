# #---------------------------single level inheritence-----------------------

# class A:
    
#     def __init__(self):
#         print("class A init")

#     def show(self):
#         print("A show")

#     def test(self):
#         print("class A test")

# class B(A):
#     def __init__(self):
#         print("class B init")
    
#     def show(self):
#         print("B show")


# obj=B()
# obj.show()
# obj.test()

# #---------------------------multilevel inheritence -------------------------------------
# class A:
#     def method_a(self):
#         print("method from A")

# class B(A):
#     def method_b(self):
#         print("method from B")

# class C(B):
#     def method_c(self):
#         print("method from C")


# obj=C()
# obj.method_b()
# obj.method_a()

#------------------------------multiple inheritence-----------------------------

# class A:
#     def method_a(self):
#         print("method from A")

#     def show(self):
#         print("A show")

# class B():
#     def method_b(self):
#         print("method from B")
    
#     def show(self):
#         print("B show")

# class C(A,B):
#     def method_c(self):
#         print("method from C")

# obj=C()
# obj.method_a()
# obj.show()
# print(C.mro())


#--------------------------------Hierarchical Inheritance-----------------------------

# class Animal:
#     def speak(self):
#         print("animal make sounds")

# class Dog(Animal):
#     def bark(self):
#         print("dog Barks")

# class Cat(Animal):
#     def meow(self):
#         print("cat meow")

# d=Dog()
# c=Cat()
# d.speak()
# d.bark()
# c.speak()
# c.meow()

#--------------------------------- init and super method ----------------------------
class A:
    def method_a(self):
        print("method of A")

class B(A):
    def __init__(self):
        print("init of B")

    def method_b(self):
        print("method of B")

class C(B):
    
    def __init__(self):
        print("init of C")
    def method_c(self):
        super().method_a()
        print("method of C")

a=A()
b=B()
c=C()
c.method_c()


