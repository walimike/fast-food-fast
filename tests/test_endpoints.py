import unittest
from flask import json
from app.views import app
from app.models import OrderList
import unittest


class EndpointsTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.test_order = {"order":"matooke"}
        self.test_order2 = {"order":"rice"}

    def tearDown(self):
        OrderList.order_list = []    

    # test for endpoints. Run using $pytest
    def test_can_get_all_orders(self):
        response = self.client.get('/fastfoodfast/v1/orders')
        self.assertEqual(response.status_code, 200)

    def test_can_make_an_order(self):
        res = self.client.post('/fastfoodfast/v1/orders', json = self.test_order)
        self.assertEqual(res.status_code, 201) 

    def test_can_not_add_multipe(self):     
        res = self.client.post('/fastfoodfast/v1/orders', json = self.test_order)
        self.assertEqual(res.status_code, 201)
        res2 = self.client.post('/fastfoodfast/v1/orders', json = self.test_order)
        self.assertEqual(len(OrderList.order_list),1)
        res3 = self.client.post('/fastfoodfast/v1/orders', json = self.test_order2)
        self.assertEqual(len(OrderList.order_list),2)

    def test_can_get_specific_order(self):
        response = self.client.get('/fastfoodfast/v1/orders/1')
        self.assertEqual(response.status_code, 404)
        self.client.post('/fastfoodfast/v1/orders', json = self.test_order , content_type='application/json')
        self.assertEqual(len(json.loads(response.data)), 1)

       
