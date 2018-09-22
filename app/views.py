from flask import Flask, jsonify, abort, request, make_response
from models import OrderList
from app import create_app
from data import check_catalogue

app = create_app(config_name='development')

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

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(406)
def not_found(error):
    return make_response(jsonify( { 'error': 'This only takes a "Yes/No" response' } ), 406)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
