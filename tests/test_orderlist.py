import unittest
from app.models import OrderList

class TestOrderList(unittest.TestCase):

    def setUp1(self):
        OrderList().add_order('rice',5000)

    def setUp2(self):
        OrderList().add_order('fish',15000)
        OrderList().add_order('maize',500)

    def tearDown(self):
        OrderList.order_list = []

    def test_can_add_order(self):
        self.assertEqual(len(OrderList.order_list), 0)
        self.setUp1()
        self.assertEqual(len(OrderList.order_list), 1)
        self.tearDown()

    def test_can_generate_unique_id(self):
        self.setUp1()
        self.assertEqual(OrderList.order_list[-1]["orderid"],1)
        self.setUp2()
        self.assertEqual(OrderList.order_list[-1]["orderid"],3)
        self.tearDown()

    def test_can_update(self):
        self.setUp2()
        OrderList().update_order(2,"yes")
        self.assertEqual(OrderList.order_list[1]['completed_status'],"Yes")
        self.tearDown()  

    def test_can_retrieve_order(self):
        self.setUp2()
        order = OrderList().retrieve_order(2)
        self.assertEqual(order["order"],"maize")      