class student:
    def __init__(self,name,rno):
        self.name=name
        self.rno=rno
    def display(self):
        print(f"{self.name} {self.rno}")
n=int(input("enter no of students"))
while(n!=0):
    name=input("enter name:")
    rno=input("enter rno:")
    e=student(name,rno)
    e.display()
    n-=1