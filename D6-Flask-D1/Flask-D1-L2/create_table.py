from app import app, db  # Import the app and db objects from your main application

# Import your models here (User, UserProfile, UploadedFile)
from user import User
from user_profile import UserProfile
from uploadedFile import UploadedFile

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        print("Database tables created successfully.")
