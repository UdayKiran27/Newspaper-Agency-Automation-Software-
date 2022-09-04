from my_package import Address
class Customer:
    def __init__(self,id="",name="",address=Address(0,0,""),phNo=0,subscriptions=[],amount=0,due=0):
        self.ID = id
        self.name = name
        self.address = address
        self.phone_number = phNo
        self.subscriptions = subscriptions
        self.amount = amount
        self.due = due
        pass