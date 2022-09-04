from my_package import User

class Deliverer(User):
    def __init__(self, id="", name="", password=""):
        self.Customers = []
        super().__init__(id, name, password)
        pass