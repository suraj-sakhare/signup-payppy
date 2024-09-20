from flask import Flask
from itsdangerous import URLSafeTimedSerializer
from src.routes import register_routes
from src.config import Config

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    from src.email_utils import init_mail
    init_mail(app)

    s = URLSafeTimedSerializer(app.secret_key)

    register_routes(app, s)

    return app
