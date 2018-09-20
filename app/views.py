from flask import Flask, jsonify, abort, request, make_response
from models import OrderList
from app import create_app
from data import check_catalogue

app = create_app(config_name='development')

# endpoint for viewing a specific order
@app.route('/fastfoodfast/v1/orders/<int:order_id>', methods=['GET'])
def get_specific_order(order_id):
    specific_order = OrderList().retrieve_order(order_id)
    if not specific_order:
        abort(404)
    return jsonify({'food_item': specific_order})
