from abc import ABC, abstractmethod
class IDatabaseOperations(ABC):
    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass

class SQLDatabase(IDatabaseOperations):
    def insert(self):
        print("Inserting into SQL db")

    def update(self):
        print("Updating SQL db")

    def delete(self):
        print("Deleting from SQL db")

class NoSQLDatabase(IDatabaseOperations):
    def insert(self):
        print("Inserting into NoSQL db")

    def update(self):
        print("Updating NoSQL db")

    def delete(self):
        print("Deleting from NoSQL db")
    
n=NoSQLDatabase()
n.insert()
n.delete()
s=SQLDatabase()
s.update()
s.delete()