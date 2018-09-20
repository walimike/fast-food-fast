import unittest

from flask import json

#Will import folder with api logic here

class EndpointsTestCase(unittest.TestCase):
    """
    Tests all endpoints for our api
    """
    def setUp(self):
        pass

    def test_can_get_all_orders(self):
        response = self.client.get('/fastfoodfast/v1/orders')
        self.assertEqual(response.status_code, 200)

    def test_whether_is_empty(self):
        response = self.client.get('/fastfoodfast/v1/orders')
        self.assertEqual(len(response), 0)

    def test_can_add_order(self):
        test_order = {"order":"chicken"}
        res = self.client.post('/fastfoodfast/v1/orders', json = test_order)
        self.assertEqual(res.status_code, 201)

    def test_can_get_specific_order(self):
        response = self.client.get('/fastfoodfast/v1/orders')
        self.assertEqual(response.status_code, 200)

    def test_can_update_order(self)
        pass
