import unittest
from app.models import OrderList

class TestOrderList(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_can_add_order(self):
        self.assertEquals(len(OrderList.order_list), 0)
        OrderList.add_order('rice',5000)
        self.assertEquals(len(OrderList.order_list), 1)

    def test_can_retrieve_order(self):
        pass
