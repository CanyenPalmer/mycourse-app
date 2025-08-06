from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    rounds = db.relationship('Round', backref='user', lazy=True)

class Round(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    course_name = db.Column(db.String(200), nullable=False)
    tee_box = db.Column(db.String(100), nullable=False)
    holes_played = db.Column(db.Integer, nullable=False)
    starting_hole = db.Column(db.Integer, nullable=False)
    total_score = db.Column(db.Integer, nullable=False)
    date_played = db.Column(db.DateTime, default=datetime.utcnow)
    notes = db.Column(db.Text, nullable=True)
    stats = db.relationship('Stat', backref='round', lazy=True)

class Stat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    round_id = db.Column(db.Integer, db.ForeignKey('round.id'), nullable=False)
    hole_number = db.Column(db.Integer, nullable=False)
    par = db.Column(db.Integer, nullable=False)
    strokes = db.Column(db.Integer, nullable=False)
    fairway_hit = db.Column(db.Boolean, nullable=True)
    green_in_regulation = db.Column(db.Boolean, nullable=True)
    putts = db.Column(db.Integer, nullable=True)

class CourseTemplate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    par_values = db.Column(db.PickleType, nullable=False)
    created_by = db.Column(db.String(120), nullable=True)

    def __repr__(self):
        return f'<CourseTemplate {self.name} | Par {sum(self.par_values)}>'
