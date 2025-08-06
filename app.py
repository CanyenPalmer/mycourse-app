from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf import CSRFProtect
from config import Config
from models import db, User, Round, CourseTemplate
from routes.auth_routes import auth_bp
from routes.round_routes import round_bp
from routes.course_routes import course_bp
from routes.dashboard_routes import dashboard_bp
from routes.analysis_routes import analysis_bp
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)

# Enable CSRF Protection
csrf = CSRFProtect(app)

# Initialize DB and create tables
db.init_app(app)
with app.app_context():
    db.create_all()

# Login management
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Register Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(round_bp)
app.register_blueprint(course_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(analysis_bp)

# Home route
@app.route("/")
def home():
    if "user_id" in session:
        return redirect(url_for("dashboard.dashboard"))
    return render_template("home.html")

# 404 error page
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Run app
if __name__ == "__main__":
    app.run(debug=True)
