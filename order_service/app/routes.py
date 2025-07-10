from flask import Blueprint, request, jsonify
from .models import Order
from .extensions import db

orders_bp = Blueprint('orders', __name__)

# GET /orders - get all orders
@orders_bp.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify([{'id': o.id, 'item': o.item, 'quantity': o.quantity} for o in orders])

# POST /orders - create new order
@orders_bp.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    new_order = Order(item=data['item'], quantity=data['quantity'])
    db.session.add(new_order)
    db.session.commit()
    return jsonify({'message': 'Order created successfully'})
