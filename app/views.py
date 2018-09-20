from flask import Flask, jsonify, abort, request, make_response
from models import OrderList
from app import create_app

app = create_app(config_name='development')

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/fastfoodfast/v1/orders', methods=['GET'])
def get_all_orders():
    return jsonify({'orderlist':OrderList().order_list})
