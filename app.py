from flask import Flask, render_template, redirect, request, session, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
import os
from config import Config
from models import db, User, Round, CourseTemplate, UserTemplate
from utils.benchmark import get_benchmark_feedback

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"

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
    return render_template("login.html")

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/dashboard")
@login_required
def dashboard():
    rounds = Round.query.filter_by(user_id=current_user.id).order_by(Round.date_played.desc()).limit(10).all()
    return render_template("dashboard.html", rounds=rounds)

@app.route("/search_course_templates")
@login_required
def search_course_templates():
    q = request.args.get("q", "")
    if not q:
        return jsonify([])

    templates = (
        CourseTemplate.query
        .filter(CourseTemplate.course_name.ilike(f"{q}%"))
        .order_by(CourseTemplate.created_count.desc())
        .limit(5)
        .all()
    )

    return jsonify([
        {"id": t.id, "course_name": t.course_name, "par_total": t.par_total}
        for t in templates
    ])

@app.route("/start_round", methods=["GET", "POST"])
@login_required
def start_round():
    if request.method == "POST":
        course_name = request.form["course_name"]
        tee_box = request.form["tee_box"]
        start_hole = int(request.form["start_hole"])
        holes_played = int(request.form["holes_played"])
        date_played = request.form["date_played"]

        course_template_id = request.form.get("course_template_id")
        if course_template_id:
            template = CourseTemplate.query.get(int(course_template_id))
            par_list = json.loads(template.par_list)
        else:
            par_list = [int(request.form[f"par_{i}"]) for i in range(1, holes_played + 1)]
            par_total = sum(par_list)

            template = CourseTemplate.query.filter_by(course_name=course_name, par_total=par_total).first()
            if template:
                template.created_count += 1
            else:
                template = CourseTemplate(course_name=course_name, par_list=json.dumps(par_list), par_total=par_total)
                db.session.add(template)

            user_template = UserTemplate(user_id=current_user.id, course_template_id=template.id,
                                         custom_name=f"Custom ({course_name}) Template | Par {par_total}")
            db.session.add(user_template)

        db.session.commit()

        session["round_info"] = {
            "course_name": course_name,
            "tee_box": tee_box,
            "start_hole": start_hole,
            "holes_played": holes_played,
            "date_played": date_played,
            "par_list": par_list
        }

        return redirect(url_for("enter_stats"))

    return render_template("round_setup.html")

@app.route("/enter_stats", methods=["GET", "POST"])
@login_required
def enter_stats():
    par_list = session["round_info"]["par_list"]
    holes_played = session["round_info"]["holes_played"_]()_]()_
