class employee:
    def __init__(self,name,id,dept):
        self.name=name
        self.id=id
        self.dept=dept
    def display(self):
        print(f"name:{self.name} id:{self.id} department:{self.dept}")
n=int(input("enter no of employees: "))
while(n!=0):
    name=input("enter name:")
    id=input("enter id:")
    dept=input("enter department: ")
    e=employee(name,id,dept)
    e.display()
    n-=1