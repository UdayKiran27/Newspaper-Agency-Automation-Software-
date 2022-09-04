from my_package import User

class Manager(User):
    def __init__(self, id="", name="", password=""):
        super().__init__(id, name, password)
        pass
