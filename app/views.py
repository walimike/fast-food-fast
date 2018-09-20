from flask import Flask, jsonify, abort, request, make_response
from models import OrderList
from app import create_app

app = create_app(config_name='development')

@app.route('/')
def index():
    return "Hello, World!"
