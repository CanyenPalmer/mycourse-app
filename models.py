# models.py

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)
    rounds = db.relationship('Round', backref='user', lazy=True)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    par_values = db.Column(db.String(255), nullable=False)  # e.g., "4,4,3,5,4,..."
    tee_box = db.Column(db.String(100))
    total_par = db.Column(db.Integer)
    holes_played = db.Column(db.Integer)
    rounds = db.relationship('Round', backref='course', lazy=True)

class Round(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(100), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    fairways_hit = db.Column(db.Integer)
    greens_in_regulation = db.Column(db.Integer)
    putts = db.Column(db.Integer)
    penalties = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=True)
