from my_package import Publication
from datetime import date
class Subscription:
    def __init__(self,publication = Publication(),fromDate=date.today(), toDate=date.today(), netDuration = 0):
        self.publication = publication
        self.from_date = fromDate
        self.to_date = toDate
        self.net_duration = netDuration
        pass