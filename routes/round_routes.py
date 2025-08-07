from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from models import db, Round, CourseTemplate
from forms import StartRoundForm
from datetime import datetime

round_bp = Blueprint("round", __name__)

@round_bp.route("/start", methods=["GET", "POST"])
@login_required
def start_round():
    form = StartRoundForm()

    if request.method == "POST" and form.validate_on_submit():
        course_name = form.course_name.data
        tee = form.tee.data
        holes = int(form.holes.data)
        par_values = request.form.getlist("par_values[]")

        if len(par_values) != holes:
            flash("Number of par values must match number of holes.", "danger")
            return render_template("start_round.html", form=form)

        try:
            par_values = [int(p) for p in par_values]
        except ValueError:
            flash("All par values must be integers.", "danger")
            return render_template("start_round.html", form=form)

        template = CourseTemplate.query.filter_by(course_name=course_name, par_values=par_values).first()
        if not template:
            template = CourseTemplate(course_name=course_name, par_values=par_values)
            db.session.add(template)

        new_round = Round(
            user_id=current_user.id,
            course_name=course_name,
            tee=tee,
            holes=holes,
            par_values=par_values,
            start_time=datetime.utcnow(),
            score_data=""
        )
        db.session.add(new_round)
        db.session.commit()

        flash("Round started successfully!", "success")
        return redirect(url_for("dashboard.dashboard"))

    return render_template("start_round.html", form=form)


@round_bp.route("/edit/<int:round_id>", methods=["GET", "POST"])
@login_required
def edit_round(round_id):
    round = Round.query.get_or_404(round_id)

    if round.user_id != current_user.id:
        flash("Unauthorized access to round.", "danger")
        return redirect(url_for("dashboard.dashboard"))

    if request.method == "POST":
        round.score_data = request.form["score_data"]
        db.session.commit()
        flash("Round updated successfully.", "success")
        return redirect(url_for("dashboard.dashboard"))

    return render_template("edit_round.html", round=round)


@round_bp.route("/delete/<int:round_id>", methods=["POST"])
@login_required
def delete_round(round_id):
    round = Round.query.get_or_404(round_id)
    if round.user_id != current_user.id:
        flash("Unauthorized to delete this round.", "danger")
        return redirect(url_for("dashboard.dashboard"))

    db.session.delete(round)
    db.session.commit()
    flash("Round deleted successfully.", "success")
    return redirect(url_for("dashboard.dashboard"))
