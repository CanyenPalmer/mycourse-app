# routes/round_routes.py

from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from models import db, Round, CourseTemplate
from forms import StartRoundForm

round_bp = Blueprint('round', __name__)

@round_bp.route('/start-round', methods=['GET', 'POST'])
@login_required
def start_round():
    form = StartRoundForm()
    if form.validate_on_submit():
        par_values = request.form.getlist('par_values[]')

        new_course = CourseTemplate(
            course_name=form.course_name.data,
            hole_pars=",".join(par_values),
            total_par=sum(map(int, par_values))
        )
        db.session.add(new_course)
        db.session.commit()

        new_round = Round(
            user_id=current_user.id,
            course_name=form.course_name.data,
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

    return render_template('start_round.html', form=form)

@round_bp.route('/round/<int:round_id>/summary')
@login_required
def round_summary(round_id):
    round_data = Round.query.get_or_404(round_id)
    return render_template('round_summary.html', round=round_data)

@round_bp.route('/_
