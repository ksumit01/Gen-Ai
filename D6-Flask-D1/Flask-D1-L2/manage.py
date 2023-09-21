from flask import Flask
from app import db  # Import db from your main app module

app = Flask(__name__)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        print("Database tables created successfully.")
