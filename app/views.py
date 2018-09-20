from flask import Flask, jsonify, abort, request, make_response
from models import OrderList
from app import create_app
from data import check_catalogue

app = create_app(config_name='development')

# endpoint for making an order
@app.route('/fastfoodfast/v1/orders', methods=['POST'])
def make_order():
    """checks whether request is in right format"""
    if not request.json or not 'order' in request.json:
        abort(400)
    recieved_order = request.get_json()

    """checks whether order is in the food catalogue"""
    if not check(recieved_order['order']):
        abort(503)
    OrderList().add_order(recieved_order['order'],check(recieved_order['order'])
    return jsonify({'orderlist': OrderList.order_list}), 201

#defining error handlers for 400 and 503

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(503)
def not_found(error):
    return make_response(jsonify({'error': 'Order does not exist, do you want to add order?'}), 503)
