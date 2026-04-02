class Laptop:
    def build(self):
        print("laptop builds")

class Desktop:
    def build(self):
        print("Desktop builds")
    
class Tablet:
    def pdf_opener(self):
        print("pdf opening...")

class Alien:
    def code(self,machine:Laptop):
        machine.build()

laptop=Laptop()
desktop=Desktop()
tablet=Tablet()
alien=Alien()
alien.code(laptop)
alien.code(desktop)
tablet.pdf_opener()