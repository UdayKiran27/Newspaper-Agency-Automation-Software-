class Address:
    def __init__(self, snumber=0, rnumber=0, hnumber=""):
        self.street_number = snumber
        self.road_number = rnumber
        self.house_number = hnumber
    def __repr__(self):
        return ("(S.No." + str(self.street_number)+" , "+"R.No." + str(self.road_number)+ " , "+ "H.No." +  str(self.house_number)+")")
        pass