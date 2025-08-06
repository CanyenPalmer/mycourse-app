# routes/analysis_routes.py

from flask import Blueprint, render_template, session, redirect, url_for
from models import Round, db
from flask_login import login_required, current_user
import matplotlib.pyplot as plt
import io
import base64

analysis_bp = Blueprint("analysis", __name__, url_prefix="/analysis")

@analysis_bp.route("/")
@login_required
def analysis_dashboard():
    user_id = current_user.id
    rounds = Round.query.filter_by(user_id=user_id).all()

    if not rounds:
        return render_template("analysis/no_data.html")

    scores = [r.total_score for r in rounds if r.total_score is not None]
    dates = [r.date.strftime("%Y-%m-%d") for r in rounds if r.date is not None]

    # Plot score trends
    fig, ax = plt.subplots()
    ax.plot(dates, scores, marker="o")
    ax.set_title("Score Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Total Score")
    ax.tick_params(axis='x', rotation=45)
    plt.tight_layout()

    # Convert plot to base64 string for embedding
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    image_base64 = base64.b64encode(buf.getvalue()).decode("utf-8")
    buf.close()

    return render_template("analysis/dashboard.html", image_base64=image_base64)
