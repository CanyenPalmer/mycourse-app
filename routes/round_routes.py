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

        new_course = CourseTemplate(
            course_name=course_name,
            hole_pars=",".join(par_values),
            total_par=sum(map(int, par_values))
        )
        db.session.add(new_course)
        db.session.commit()

        new_round = Round(
            user_id=current_user.id,
            course_name=course_name,
            total_par=new_course.total_par,
            total_score=0,
            fairways_hit=0,
            greens_in_reg=0,
            putts=0,
            penalties=0,
            notes=""
        )
        db.session.add(new_round)
        db.session.commit()

        return redirect(url_for('round.edit_round', round_id=new_round.id))

    return render_template('start_round.html')

@round_bp.route('/round/<int:round_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_round(round_id):
    round_data = Round.query.get_or_404(round_id)

    if request.method == 'POST':
        round_data.total_score = int(request.form.get('total_score', 0))
        round_data.fairways_hit = int(request.form.get('fairways_hit', 0))
        round_data.greens_in_reg = int(request.form.get('greens_in_reg', 0))
        round_data.putts = int(request.form.get('putts', 0))
        round_data.penalties = int(request.form.get('penalties', 0))
        round_data.notes = request.form.get('notes', '')
        db.session.commit()
        return redirect(url_for('round.round_summary', round_id=round_data.id))

    return render_template('edit_round.html', round=round_data)

@round_bp.route('/round/<int:round_id>/summary')
@login_required
def round_summary(round_id):
    round_data = Round.query.get_or_404(round_id)
    return render_template('round_summary.html', round=round_data)

@round_bp.route('/past_rounds')
@login_required
def past_rounds():
    user_rounds = Round.query.filter_by(user_id=current_user.id).order_by(Round.date_played.desc()).all()
    return render_template('past_rounds.html', rounds=user_rounds)

