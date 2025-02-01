class car:
    def move(self):
        print("The car is driving on the road.")

class airplane:
    def move(self):
        print("The airplane is flying in the sky.")

class flyingCar(car, airplane):
    def move(self):
        print("The flying car can:")
        car.move(self)
        airplane.move(self)

flying_car = flyingCar()
flying_car.move()
