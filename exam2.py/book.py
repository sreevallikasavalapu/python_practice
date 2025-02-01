class Book:
    def __init__(self, title):
        self.title = title

    def add(self, other):
        if isinstance(other, Book):  
            return Book(f"{self.title} and {other.title}")
        raise TypeError("Can only add Book instances together")

    def __str__(self):
        return self.title

b1 = Book("Harry Potter")
b2 = Book("It ends with us")
b3 = b1.add(b2)  
print(b3)  