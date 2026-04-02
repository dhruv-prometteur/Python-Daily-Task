class A:
    def show(self):
        print("Show of A")

class B(A):
    def show(self):
        print("Show of B")

obj=B()
obj.show()