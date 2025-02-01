class book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
    def display(self):
        print(f"{self.title} {self.author} {self.isbn}")
n=int(input("enter no of books: "))
while(n!=0):
    title=input("enter title: ")
    author=input("enter author: ")
    isbn=input("enter isbn: ")
    e=book(title,author,isbn)
    e.display()
    n-=1