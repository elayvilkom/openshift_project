from flask import Flask
from .extensions import db
from .routes import orders_bp

def create_app():
    app = Flask(__name__)

    # Database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dbuser:123456@postgres-order:5432/ordersdb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(orders_bp)

    # Create tables
    with app.app_context():
        db.create_all()

    return app
