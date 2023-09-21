from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Define your database configuration
# db_config = {
#     'username': 'root',
#     'password': 'root@123',
#     'host': 'localhost',  # Replace '123@localhost' with 'localhost'
#     'database_name': 'GA201'
# }

# Create the database URI
# app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqlconnector://{db_config['username']}:{db_config['password']}@{db_config['host']}/{db_config['database_name']}"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# Initialize the SQLAlchemy extension
db = SQLAlchemy(app)

if __name__ == '__main__':
    with app.app_context():
        # Create the database tables
        db.create_all()
