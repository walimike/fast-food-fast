from flask import Flask, jsonify, abort, request, make_response
from .models import OrderList
from . import create_app
from .data import check_catalogue

app = create_app(config_name='development')

"""This route provides a welcome message for our api"""
@app.route('/')
def index():
    return "<h1> Welcome to Fast Food Fast </h1>"

"""This endpoint fetches all orders, returns empty list, if no order in list"""
@app.route('/v1/orders/', methods=['GET'])
def get_all_orders():
    return jsonify({'orderlist':OrderList().order_list})

"""This endpoint fetches a specific order based on the ID provided"""
@app.route('/v1/orders/<int:order_id>', methods=['GET'])
def get_specific_order(order_id):
    specific_order = OrderList().retrieve_order(order_id)
    if not specific_order:
        abort(404)
    return jsonify({'food_item': specific_order})

"""This endpoint is for making an order"""
@app.route('/v1/orders/', methods=['POST'])
def make_order():
    """checks whether request is in right format"""
    if not request.json or not 'order' in request.json:
        abort(400)
    recieved_order = request.get_json()['order']

    """checks whether order is in the food catalogue"""
    if not check_catalogue(recieved_order):
        abort(503)

    """Checks if order is repeated"""
    if not len(OrderList.order_list) == 0 and OrderList.order_list[-1]["order"] == recieved_order:
        abort(403)
          
    OrderList().add_order(recieved_order,check_catalogue(recieved_order))
    return jsonify({'orderlist': OrderList.order_list}), 201

"""This endpoint is for updating the completion status for an order"""
@app.route('/v1/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    if not type(order_id)==int:
        abort(400)

    """checks the the json data is inthe right format and has the right key word"""    
    if not request.json or not 'completed_status' in request.json:
        abort(400)      
    new_status =  request.get_json()['completed_status']
    
    """checks that the order ID does not exceed the maximum ID"""
    if order_id > OrderList().id_limit():
        return jsonify({"error":"ID out of range"})

    """checks that our completed status is either yes or no"""    
    if new_status.lower() != "yes":
        if new_status.lower() != "no":
            abort(406)
    OrderList().update_order(order_id,new_status)
    return jsonify({'orderlist':OrderList.order_list})
    

 # error handlers
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(406)
def wrong_format(error):
    return make_response(jsonify( { 'error': 'This only takes a "Yes/No" response' } ), 406)


@app.errorhandler(403)
def repeat_order(error):
    return make_response(jsonify( { 'error': 'You seem to be repeating the order' } ), 403)

@app.errorhandler(503)
def no_order(error):
    return make_response(jsonify( { 'error': 'Order not currently in order list' } ), 503) 
 
