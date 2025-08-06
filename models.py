from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    rounds = db.relationship("Round", backref="user", lazy=True)

class Round(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    course_name = db.Column(db.String(120), nullable=False)
    date_played = db.Column(db.DateTime, default=datetime.utcnow)
    total_score = db.Column(db.Integer, nullable=False)
    total_par = db.Column(db.Integer, nullable=False)
    fairways_hit = db.Column(db.Integer)
    greens_in_reg = db.Column(db.Integer)
    putts = db.Column(db.Integer)
    penalties = db.Column(db.Integer)
    notes = db.Column(db.Text)

class CourseTemplate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(120), nullable=False)
    total_par = db.Column(db.Integer, nullable=False)
    hole_pars = db.Column(db.String(120), nullable=False)  # e.g., "4,4,3,5,4,4,3,5,4"

    def __repr__(self):
        return f"<CourseTemplate {self.course_name} | Par {self.total_par}>"
