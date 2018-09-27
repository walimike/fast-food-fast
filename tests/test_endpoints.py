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
        self.test_order3 = {"order":"chips"}
        self.test_status1 = {"completed_status":"yes"}

    def tearDown(self):
        OrderList.order_list = []    

    # test for endpoints. Run using $pytest
    def test_can_get_all_orders(self):
        response = self.client.get('/v1/orders')
        self.assertEqual(response.status_code, 200)

    def test_can_make_an_order(self):
        res = self.client.post('/v1/orders', json = self.test_order)
        self.assertEqual(res.status_code, 201) 

    def test_can_not_repeat_order(self):
        self.assertEqual(len(OrderList.order_list),0)     
        res = self.client.post('/v1/orders', json = self.test_order)
        self.assertEqual(res.status_code, 201)
        res2 = self.client.post('/v1/orders', json = self.test_order)
        self.assertEqual(len(OrderList.order_list),1)
        res3 = self.client.post('/v1/orders', json = self.test_order2)
        self.assertEqual(len(OrderList.order_list),2)

    def test_can_get_specific_order(self):
        response = self.client.get('/v1/orders/1')
        self.assertEqual(response.status_code, 404)
        self.client.post('/v1/orders', json = self.test_order , content_type='application/json')
        self.assertEqual(len(json.loads(response.data)), 1)

    def test_can_not_add_unknown_food(self):
        res = self.client.post('/v1/orders', json = self.test_order3)
        self.assertEqual(res.status_code, 503)

    def test_for_id_out_of_range(self):
        res = self.client.post('/v1/orders', json = self.test_order)
        res2 = self.client.post('/v1/orders', json = self.test_order2)
        response = self.client.get('/v1/orders/1')
        self.assertEqual(response.status_code, 200)
        response2 = self.client.get('/v1/orders/3')
        self.assertEqual(response2.status_code, 404)

    def test_can_update_status(self):
        res = self.client.post('/v1/orders', json = self.test_order)   
        response = self.client.put('/v1/orders/1', json = self.test_status1)
        self.assertEqual(response.status_code, 200)