from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Round(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    course_name = db.Column(db.String(120))
    tee_box = db.Column(db.String(50))
    date_played = db.Column(db.String(20))
    strokes = db.Column(db.PickleType)  # list of strokes per hole
    putts = db.Column(db.PickleType)    # list of putts per hole
    pars = db.Column(db.PickleType)     # list of par values

class CourseTemplate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(128))
    par_list = db.Column(db.Text)  # JSON-encoded list of pars
    par_total = db.Column(db.Integer)
    created_count = db.Column(db.Integer, default=1)

class UserTemplate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    course_template_id = db.Column(db.Integer, db.ForeignKey("course_template.id"))
    custom_name = db.Column(db.String(256))
