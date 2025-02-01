from abc import ABC, abstractmethod

class Payment(ABC):
    # @abstractmethod
    def process_payment(self):
        pass

class CreditCardPayment(Payment):
    def process_payment(self):
        print("Processing credit card payment")

class PayPalPayment(Payment):
    def process_payment(self):
        print("Processing PayPal payment")

class BitcoinPayment(Payment):
    def process_payment(self):
        print("Processing Bitcoin payment")
        
b=BitcoinPayment()
b.process_payment()
p=PayPalPayment()
p.process_payment()
c=CreditCardPayment()
c.process_payment()
