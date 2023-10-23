class Animal:
    def __init__(self, name):
        self.name = name
    
    def nourrir(self):
        print(f"Je nourris {self.name}")
        print(f"Preparer sa nourriture")
        print(f"Verifier s'il est vivant")

class Chat(Animal):
    def nourrir(self):
        super().nourrir()
        print("Petits câlins <3")

class Requin(Animal):   
    def nourrir(self):
        # super().nourrir()
        print("Restons à distance...")
    
un_chat = Chat("Miaou")
un_requin = Requin("Flipper")

un_chat.nourrir()
print("-------")
un_requin.nourrir()