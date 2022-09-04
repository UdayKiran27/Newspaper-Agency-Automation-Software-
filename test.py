import unittest
from  my_package import *
from datetime import date
# import main


class TestAddress(unittest.TestCase):
    def setUp(self):
        self.address1=Address(1,1,"h1")
        # self.address2=Address(1)
    def test_address(self):
        self.assertEqual(self.address1.street_number,1)
        self.assertEqual(self.address1.road_number,1)
        self.assertEqual(self.address1.house_number,"h1")
class TestPublication(unittest.TestCase):
    def setUp(self) -> None:
        self.publication=Publication("000010","magazine1","Newspaper","English",10.0)
    def test_publication(self):
        self.assertEqual(self.publication.paper_id,"000010")
        self.assertEqual(self.publication.paper_name,"magazine1")
        self.assertEqual(self.publication.paper_type,"Newspaper")
        self.assertEqual(self.publication.language,"English")
        self.assertEqual(self.publication.price,10.0)
class TestSubscription(unittest.TestCase):
    def setUp(self) -> None:
        self.subscription1=Subscription(Publication("003000","magazine4","Magazine","Telugu",50.0),date(2020,8,12),date(2020,12,2),
                                        0)
    def test_subscription(self):
        self.assertEqual(self.subscription1.publication.paper_id,"003000")
        self.assertEqual(self.subscription1.publication.paper_name, "magazine4")
        self.assertEqual(self.subscription1.publication.paper_type, "Magazine")
        self.assertEqual(self.subscription1.publication.language, "Telugu")
        self.assertEqual(self.subscription1.publication.price, 50.0)
        self.assertEqual(self.subscription1.from_date,date(2020,8,12))
        self.assertEqual(self.subscription1.to_date,date(2020,12,2))
        self.assertEqual(self.subscription1.net_duration,0)

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer=Customer("123678","Rohan",Address(1,1,"h2"),"7712346613",[],0,0)
        # self.customer1=Customer("001000","Rohan",Address(1,1,2),[Subscription(Publication("000001","magazine1","magazine","English",10.0),date(2020,8,15),date(2020,12,2),0)],0,0)
    def test_something(self):
        self.assertEqual(self.customer.ID,"123678")
        self.assertEqual(self.customer.name,"Rohan")
        self.assertEqual(self.customer.address.street_number,1)
        self.assertEqual(self.customer.address.road_number, 1)
        self.assertEqual(self.customer.address.house_number, "h2")
        self.assertEqual(self.customer.phone_number,"7712346613")
        self.assertEqual(self.customer.subscriptions,[])
        self.assertEqual(self.customer.amount,0)
        self.assertEqual(self.customer.due,0)
class TestManager(unittest.TestCase):
    def setUp(self) -> None:
        self.manager=Manager("003150","Manager","@1234")
    def test_manager(self):
        self.assertEqual(self.manager.ID,"003150")
        self.assertEqual(self.manager.name,"Manager")
        self.assertEqual(self.manager.password,"@1234")
class TestDeliverer(unittest.TestCase):
    def setUp(self) -> None:
        self.deliverer=Deliverer("123456","ABCDEF","deli@123")
    def test_deliverer(self):
        self.assertEqual(self.deliverer.ID,"123456")
        self.assertEqual(self.deliverer.name,"ABCDEF")
        self.assertEqual(self.deliverer.password,"deli@123")

if __name__ == '__main__':
    unittest.main()
