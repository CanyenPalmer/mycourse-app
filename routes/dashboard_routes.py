from flask import Blueprint, render_template, session, redirect, url_for
from flask_login import login_required, current_user
from models import db, Round
import matplotlib.pyplot as plt
import io
import base64

dashboard_bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")

@dashboard_bp.route("/")
@login_required
def dashboard():
    # Get last 10 rounds for line graph
    user_id = current_user.id
    rounds = (
        Round.query.filter_by(user_id=user_id)
        .order_by(Round.date_played.desc())
        .limit(10)
        .all()
    )

    rounds.reverse()  # Make oldest first for line plot
    dates = [r.date_played.strftime("%m-%d") for r in rounds]
    score_diffs = [r.total_score - r.total_par for r in rounds]

    # Generate line graph
    img = io.BytesIO()
    plt.figure(figsize=(6, 3))
    plt.plot(dates, score_diffs, marker="o")
    plt.axhline(0, color="gray", linestyle="--")
    plt.title("Performance Trend (Score vs Par)")
    plt.xlabel("Date")
    plt.ylabel("Strokes vs Par")
    plt.tight_layout()
    plt.grid(True)
    plt.savefig(img, format="png")
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode("utf8")
    plt.close()

    # Most recent round summary
    latest_round = (
        Round.query.filter_by(user_id=user_id)
        .order_by(Round.date_played.desc())
        .first()
    )

    return render_template(
        "dashboard.html",
        plot_url=plot_url,
        latest_round=latest_round,
    )
