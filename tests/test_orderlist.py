import unittest
from app.models import OrderList

class TestOrderList(unittest.TestCase):

    def setUp1(self):
        OrderList().add_order('rice',5000)

    def setUp2(self):
        OrderList().add_order('fish',15000)
        OrderList().add_order('maize',500)

    def tearDown(self):
        pass

    def test_can_add_order(self):
        self.assertEquals(len(OrderList.order_list), 0)
        self.setUp1()
        self.assertEquals(len(OrderList.order_list), 1)

    def test_can_retrieve_order(self):


    def test_can_generate unique_id(self):
        self.setUp1
        self.assertEquals(OrderList.order_list[-1]["orderid"],1)
        self.setUp2
        self.assertEquals(OrderList.order_list[-1]["orderid"],3)

    def test_cannot_add_same_subsequent_order(self):
        self.setUp()
        self.assertEquals(OrderList.order_list[-1]["order"],"rice")
        self.setUp2
        OrderList().add_order('matooke',5000)
        OrderList().add_order('matooke',5000)
        self.assertEquals(len(OrderList.order_list),4)
        self.assertEquals(OrderList.order_list[-2]["order"],"maize")
