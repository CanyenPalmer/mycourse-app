from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class StartRoundForm(FlaskForm):
    course_name = StringField('Course Name', validators=[DataRequired()])
    tee_box = SelectField('Tee Box', choices=[('Blue', 'Blue'), ('White', 'White'), ('Red', 'Red')], validators=[DataRequired()])
    num_holes = SelectField('Number of Holes', choices=[('9', '9'), ('18', '18')], validators=[DataRequired()])
    submit = SubmitField('Start Round')
