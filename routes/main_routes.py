# routes/main_routes.py

from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from models import db, Round, Course
from datetime import datetime

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('index.html')

@main_bp.route('/dashboard')
@login_required
def dashboard():
    user_rounds = Round.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', rounds=user_rounds)

@main_bp.route('/add-round', methods=['GET', 'POST'])
@login_required
def add_round():
    if request.method == 'POST':
        score = request.form['score']
        fairways = request.form.get('fairways_hit', 0)
        gir = request.form.get('greens_in_regulation', 0)
        putts = request.form.get('putts', 0)
        penalties = request.form.get('penalties', 0)
        date = datetime.now().strftime('%Y-%m-%d')
        new_round = Round(score=score, fairways_hit=fairways, greens_in_regulation=gir,
                          putts=putts, penalties=penalties, date=date, user_id=current_user.id)
        db.session.add(new_round)
        db.session.commit()
        flash('Round added successfully!')
        return redirect(url_for('main.dashboard'))
    return render_template('add_round.html')

