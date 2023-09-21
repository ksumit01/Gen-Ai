from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True, nullable=False)
    bio = db.Column(db.String(250))
    profile_picture = db.Column(db.String(250))

    user = db.relationship('User', backref='profile', uselist=False)

    def __init__(self, user_id, bio=None):
        self.user_id = user_id
        self.bio = bio
