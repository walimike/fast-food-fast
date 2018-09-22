from flask import Flask, jsonify, abort, request, make_response
from models import OrderList
from app import create_app
from data import check_catalogue

app = create_app(config_name='development')

#welcome message for user.
@app.route('/')
def index():
    return "<h1> Welcome to Fast Food Fast"

#fetches all orders, returns empty list, if none
@app.route('/fastfoodfast/v1/orders', methods=['GET'])
def get_all_orders():
    return jsonify({'orderlist':OrderList().order_list})

# fetches a specific order
@app.route('/fastfoodfast/v1/orders/<int:order_id>', methods=['GET'])
def get_specific_order(order_id):
    specific_order = OrderList().retrieve_order(order_id)
    if not specific_order:
        abort(404)
    return jsonify({'food_item': specific_order})

# endpoint for making an order
@app.route('/fastfoodfast/v1/orders', methods=['POST'])
def make_order():
    """checks whether request is in right format"""
    if not request.json or not 'order' in request.json:
        abort(400)
    recieved_order = request.get_json()['order']

    """checks whether order is in the food catalogue"""
    if not check_catalogue(recieved_order):
        abort(503)
    OrderList().add_order(recieved_order,check_catalogue(recieved_order))
    return jsonify({'orderlist': OrderList.order_list}), 201


# endpoint for updating the completion status for an order
@app.route('/fastfoodfast/v1/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    if not type(order_id)==int:
        abort(400)
    if order_id<1 or order_id>(OrderList().id_limit()):
        abort(404)
    if not request.json and not (request.json()['completed_status']).isalpha():
        abort(400)
    new_status =  request.get_json()['completed_status'])
    if new_status.lower() != ("yes" or "no"):
        abort(406)
    OrderList().update_order(order_id,new_status)
    return jsonify({'orderlist':OrderList.order_list})

 # error handlers
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

  @app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(406)
def not_found(error):
    return make_response(jsonify( { 'error': 'This only takes a "Yes/No" response' } ), 406)
