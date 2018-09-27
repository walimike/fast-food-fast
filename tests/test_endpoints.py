import unittest
from flask import json
from app.views import app
from app.models import OrderList
import unittest


class EndpointsTestCase(unittest.TestCase):
    """
    Tests our API endpoints, run using pytest.
    """
    def setUp(self):
        self.client = app.test_client()
        self.test_order = {"order":"matooke"}
        self.test_order2 = {"order":"rice"}
        self.test_order3 = {"order":"chips"}
        self.test_status1 = {"completed_status":"yes"}

    def tearDown(self):
        OrderList.order_list = []    

    def test_can_get_all_orders(self):
        """Tests whether endpoint can get all orders."""
        response = self.client.get('/v1/orders')
        self.assertEqual(response.status_code, 200)

    def test_can_make_an_order(self):
        """Tests whether user can post an order."""
        res = self.client.post('/v1/orders', json = self.test_order)
        self.assertEqual(res.status_code, 201) 

    def test_can_not_repeat_order(self):
        """Checks original length of orderlist is zero."""
        self.assertEqual(len(OrderList.order_list),0)     
        res = self.client.post('/v1/orders', json = self.test_order)
        self.assertEqual(res.status_code, 201)
        """Repeats test_order subsequently."""
        res2 = self.client.post('/v1/orders', json = self.test_order)
        """Checks that length is still 1 even after posting same order twice."""
        self.assertEqual(len(OrderList.order_list),1)
        res3 = self.client.post('/v1/orders', json = self.test_order2)
        self.assertEqual(len(OrderList.order_list),2)

    def test_can_get_specific_order(self):
        """Tests whether endpoint can return one order based on ID."""
        response = self.client.get('/v1/orders/1')
        self.assertEqual(response.status_code, 404)
        self.client.post('/v1/orders', json = self.test_order , content_type='application/json')
        self.assertEqual(len(json.loads(response.data)), 1)

    def test_can_not_add_unknown_food(self):
        """Tests that user can not make an order for commodity not on catalogue"""
        res = self.client.post('/v1/orders', json = self.test_order3)
        self.assertEqual(res.status_code, 503)

    def test_for_id_out_of_range(self):
        """Tests that app raises error for ID out of range"""
        res = self.client.post('/v1/orders', json = self.test_order)
        res2 = self.client.post('/v1/orders', json = self.test_order2)
        response = self.client.get('/v1/orders/1')
        self.assertEqual(response.status_code, 200)
        response2 = self.client.get('/v1/orders/3')
        self.assertEqual(response2.status_code, 404)

    def test_can_update_status(self):
        """Tets whether status code for updating is 200"""
        res = self.client.post('/v1/orders', json = self.test_order)   
        response = self.client.put('/v1/orders/1', json = self.test_status1)
        self.assertEqual(response.status_code, 200)
        
    def test_can_change_status_update(self):
        """Tests that the status changes from yes to know"""
        res = self.client.post('/v1/orders', json = self.test_order)
        order_status = OrderList.order_list[0]["completed_status"]
        self.assertEqual(order_status,"No") 
        response = self.client.put('/v1/orders/1', json = self.test_status1)
        order_status2 = OrderList.order_list[0]["completed_status"]
        self.assertEqual(order_status2,"Yes")  

    def test_can_not_get_order_beyond_id_limit(self):
        response = self.client.get('/v1/orders/1')
        self.assertEqual(response.status_code,404)
        response2 = self.client.get('/v1/orders/-1')     
        self.assertEqual(response.status_code,404)

    def test_must_have_right_keyword(self):
        """Tests whether json data has right key word"""
        data = {"ordr":"rice"}    
        res = self.client.post('/v1/orders', json = data)
        self.assertEqual(res.status_code,400)


