from abc import ABC,abstractmethod


class PaymentGateway(ABC):

    @abstractmethod
    def pay(self):
        pass


class RazorPay(PaymentGateway):
    
    def pay(self):
        print("paying with razorpay...")

class PayPal(PaymentGateway):
    def pay(Self):
        print("paying with PayPal")

class Purchase():
    def __init__(self,getway):
        self.getway=getway

    def checkout(self):
        print("checking out...")
        self.getway.pay()

razorpay=RazorPay()
paypal=PayPal()
purchase=Purchase(razorpay)
purchase.checkout()



        
        