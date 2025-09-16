import os
from flask import Flask, jsonify
from .config import Config
from .db import db, init_db
from .logger import setup_logging
from .exceptions import AppError

def create_app(config_object: Config = None):
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config_object or Config())

    # Logging
    setup_logging(app.config)

    # Initialize DB
    db.init_app(app)
    with app.app_context():
        init_db(app)

    # Register blueprints / routes
    from .routes import bp as routes_bp
    app.register_blueprint(routes_bp, url_prefix="/api")

    # Centralized exception handling
    @app.errorhandler(AppError)
    def handle_app_error(exc):
        response = {"error": exc.message}
        return jsonify(response), exc.status_code

    @app.errorhandler(400)
    def bad_request(e):
        return jsonify({"error": "Bad Request"}), 400

    @app.errorhandler(404)
    def not_found(e):
        return jsonify({"error": "Not Found"}), 404

    @app.errorhandler(500)
    def server_error(e):
        return jsonify({"error": "Internal Server Error"}), 500

    return app
