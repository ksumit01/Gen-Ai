from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Import and register your blueprints here
from app.routes.admin import admin_bp
# from app.routes.customer import customer_bp
# from app.routes.auth import auth_bp
# from app.routes.api import api_bp

app.register_blueprint(admin_bp)
# app.register_blueprint(customer_bp)
# app.register_blueprint(auth_bp)
# app.register_blueprint(api_bp)

# Other app initialization code
