from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from models import db, User, Round, CourseTemplate
from utils.benchmark import get_benchmark_feedback
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.config.from_object("config.Config")

db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@app.before_first_request
def create_tables():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return "User already exists."

        user = User(email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for("dashboard"))
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for("dashboard"))
        return "Invalid credentials."
    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/dashboard")
@login_required
def dashboard():
    rounds = Round.query.filter_by(user_id=current_user.id).order_by(Round.id.desc()).limit(10).all()
    return render_template("dashboard.html", rounds=rounds)

@app.route("/start-round", methods=["GET", "POST"])
@login_required
def start_round():
    if request.method == "POST":
        course_name = request.form["course_name"]
        tee_box = request.form["tee_box"]
        start_hole = int(request.form["start_hole"])
        holes_played = int(request.form["holes_played"])
        date_played = request.form["date_played"]

        par_list = []
        for i in range(1, 19):
            par_val = request.form.get(f"par_{i}")
            if par_val:
                par_list.append(int(par_val))

        session["round_info"] = {
            "course_name": course_name,
            "tee_box": tee_box,
            "start_hole": start_hole,
            "holes_played": holes_played,
            "date_played": date_played,
            "par_list": par_list,
        }
        return redirect(url_for("round_stats"))

    return render_template("round_setup.html")

@app.route("/round-stats", methods=["GET", "POST"])
@login_required
def round_stats():
    round_info = session.get("round_info")
    par_list = round_info.get("par_list")
    holes_played = round_info.get("holes_played")

    if request.method == "POST":
        strokes = []
        putts = []
        for i in range(holes_played):
            strokes.append(int(request.form[f"strokes_{i}"]))
            putts.append(int(request.form[f"putts_{i}"]))

        new_round = Round(
            user_id=current_user.id,
            course_name=round_info["course_name"],
            tee_box=round_info["tee_box"],
            date_played=round_info["date_played"],
            strokes=strokes,
            putts=putts,
            pars=par_list[:holes_played]
        )
        db.session.add(new_round)
        db.session.commit()

        session.pop("round_info", None)
        session["last_round_id"] = new_round.id

        return redirect(url_for("round_summary"))

    return render_template("round_stats.html", par_list=par_list[:holes_played])

@app.route("/round-summary")
@login_required
def round_summary():
    round_id = session.get("last_round_id")
    if not round_id:
        return redirect(url_for("dashboard"))

    round_obj = Round.query.get_or_404(round_id)
    feedback = get_benchmark_feedback(round_obj)

    return render_template("round_summary.html", round=round_obj, feedback=feedback)

if __name__ == "__main__":
    app.run()

