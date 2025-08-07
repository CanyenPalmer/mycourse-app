# forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo

class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

class StartRoundForm(FlaskForm):
    course_name = StringField("Course Name", validators=[DataRequired()])
    tee = SelectField("Tee", choices=[("Back", "Back"), ("Middle", "Middle"), ("Front", "Front")], validators=[DataRequired()])
    holes = SelectField("Number of Holes", choices=[("9", "9"), ("18", "18")], validators=[DataRequired()])
    submit = SubmitField("Start Round")
