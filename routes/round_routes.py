# routes/round_routes.py

from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from models import db, Round, CourseTemplate

round_bp = Blueprint('round', __name__)

@round_bp.route('/start-round', methods=['GET', 'POST'])
@login_required
def start_round():
    if request.method == 'POST':
        course_name = request.form['course_name']
        par_values = request.form.getlist('par_values[]')
        tee = request.form['tee']
        holes = int(request.form['holes'])

        new_course = Course(name=course_name, pars=",".join(par_values))
        db.session.add(new_course)
        db.session.commit()

        new_round = Round(user_id=current_user.id, course_id=new_course.id, tee=tee, holes=holes)
        db.session.add(new_round)
        db.session.commit()

        return redirect(url_for('round.edit_round', round_id=new_round.id))

    return render_template('start_round.html')

@round_bp.route('/round/<int:round_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_round(round_id):
    round_data = Round.query.get_or_404(round_id)

    if request.method == 'POST':
        round_data.score_data = request.form['score_data']
        db.session.commit()
        return redirect(url_for('main.dashboard'))

    return render_template('edit_round.html', round=round_data)

@round_bp.route('/round/<int:round_id>/summary')
@login_required
def round_summary(round_id):
    round_data = Round.query.get_or_404(round_id)
    return render_template('round_summary.html', round=round_data)
