class Electronics:
    def __init__(self, brand):
        self.brand = brand

    def display_info(self):
        print(f"Brand: {self.brand}")

class MobileDevice(Electronics):
    def __init__(self, brand, battery_life):
        super().__init__(brand)
        self.battery_life = battery_life

    def display_info(self):
        super().display_info()
        print(f"Battery Life: {self.battery_life} hours")
        
class SmartPhone(MobileDevice):
    def __init__(self, brand, battery_life, os):
        super().__init__(brand, battery_life)
        self.os = os

    def display_info(self):
        super().display_info()
        print(f"Operating System: {self.os}")

phone = SmartPhone("Oneplus", 24, "Android")
phone.display_info()
