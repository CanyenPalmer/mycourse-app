# models.py
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

# Initialize database
db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"

class Round(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date_played = db.Column(db.DateTime, nullable=False)
    score = db.Column(db.Integer)
    # Add any additional fields required for your golf rounds here

class CourseTemplate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(128), nullable=False)
    par_data = db.Column(db.Text, nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'))

