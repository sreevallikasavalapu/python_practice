class vehicle:
    def display(self):
        print("vehicle is base class")
class car(vehicle):
    def display(self):
        print("this is car class")
class bike(vehicle):
    def display(self):
        print("this is bike class")
class electric_car(car):
    def display(self):
        print("this is base class of car")
e=electric_car()
e.display()
b=bike()
b.display()
c=car()
c.display()
v=vehicle()
v.display()