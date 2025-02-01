from abc import ABC ,abstractmethod
class Notification(ABC):
    @abstractmethod
    def send(self):
        pass

class EmailNotification(Notification):
    def send(self):
        print("Sending email notification")

class SMSNotification(Notification):
    def send(self):
        print("Sending SMS notification")
        
s=SMSNotification()
s.send()
e=EmailNotification()
e.send()
