from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    rounds = db.relationship('Round', backref='user', lazy=True)

class Round(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date_played = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    course_name = db.Column(db.String(100), nullable=False)
    total_score = db.Column(db.Integer, nullable=False)
    total_par = db.Column(db.Integer, nullable=False)
    fairways_hit = db.Column(db.Integer, default=0)
    greens_in_reg = db.Column(db.Integer, default=0)
    putts = db.Column(db.Integer, default=0)
    penalties = db.Column(db.Integer, default=0)
