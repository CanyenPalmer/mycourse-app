@dashboard_bp.route('/')
@dashboard_bp.route('/dashboard')
@login_required
def dashboard():
    latest_round = Round.query.filter_by(user_id=current_user.id).order_by(Round.date_played.desc()).first()
    last_10_rounds = Round.query.filter_by(user_id=current_user.id).order_by(desc(Round.date_played)).limit(10).all()

    dates = [r.date_played.strftime('%m-%d') for r in reversed(last_10_rounds)]
    scores = [r.total_score for r in reversed(last_10_rounds)]
    pars = [r.total_par for r in reversed(last_10_rounds)]

    plt.figure(figsize=(8, 4))
    plt.plot(dates, scores, marker='o', label='Score', linestyle='-')
    plt.plot(dates, pars, marker='x', label='Par', linestyle='--')
    plt.xlabel('Date')
    plt.ylabel('Strokes')
    plt.title('Score vs Par (Last 10 Rounds)')
    plt.legend()
    plt.tight_layout()

    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    plt.close()

    return render_template("dashboard.html", latest_round=latest_round, plot_url=plot_url)
