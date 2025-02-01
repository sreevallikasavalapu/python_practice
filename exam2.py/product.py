class product:
    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock
    def check_availability(self,qt):
        if qt<=self.stock:
            print("quantity is available")
        else:
            print("quantity is not available")
p=product("cotton",70,100)
n=int(input("enter quantity to check the availability"))
p.check_availability(n)