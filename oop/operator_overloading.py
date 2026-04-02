class Account:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    def __str__(self):
        return f"Name : {self.name},Balance : {self.balance}"
    
    def __add__(self, other):
        return self.balance + other.balance
    
    def __gt__(self, other):
        return self.balance > other.balance

dhruv=Account("Dhruv",2000)
roman=Account("Roman",4000)

combined=dhruv+roman
print(combined)
print(dhruv)
print(roman)

if dhruv > roman:
    print(f"{dhruv.name} pays the bill")

else:
    print(f"{roman.name} pays the bill")

    