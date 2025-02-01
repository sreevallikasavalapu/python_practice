from abc import ABC, abstractmethod

class UserAuthentication(ABC):
    @abstractmethod
    def login(self, username, password):
        pass

    @abstractmethod
    def logout(self):
        pass

class GoogleAuth(UserAuthentication):
    def login(self, username, password):
        print(f"{username} logged in via Google")

    def logout(self):
        print("Logged out from Google")

class FacebookAuth(UserAuthentication):
    def login(self, username, password):
        print(f"{username} logged in via Facebook")

    def logout(self):
        print("Logged out from Facebook")
        
g=GoogleAuth()
g.login("valli_123","vallii@45")
g.logout()
f=FacebookAuth()
f.login("riya_0987","riyaaaaz21")
f.logout()
