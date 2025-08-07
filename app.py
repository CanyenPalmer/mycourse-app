from flask import Flask
from flask_login import LoginManager
from extensions import db
from models import User
from routes.auth_routes import auth
from routes.dashboard_routes import dashboard_bp
from routes.round_routes import round_bp

app = Flask(__name__)
app.config.from_object('config.Config')

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Register blueprints
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(dashboard_bp, url_prefix='/')      # ✅ Show dashboard at '/'
app.register_blueprint(round_bp, url_prefix='/rounds')

