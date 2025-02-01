class animal:
    def speak(self):
        pass
class dog(animal):
    def speak(self):
        print("bow bow")
class cat(animal):
    def speak(self):
        print("meow meow")
c=cat()
c.speak()
d=dog()
d.speak()