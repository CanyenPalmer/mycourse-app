def get_benchmark_feedback(round_obj):
    strokes = round_obj.strokes
    putts = round_obj.putts
    pars = round_obj.pars

    total_strokes = sum(strokes)
    total_putts = sum(putts)
    total_par = sum(pars)

    stats = {
        "score": total_strokes,
        "putts": total_putts,
        "par": total_par
    }

    benchmarks = {
        "Top 100": {"score": total_par + 3, "putts": 32},
        "Top 50": {"score": total_par + 1, "putts": 30},
        "Top 10": {"score": total_par - 1, "putts": 28},
    }

    feedback = "Solid round! Keep sharpening all parts of your game."

    if total_putts > benchmarks["Top 100"]["putts"]:
        feedback = "Too many 3 putts! Work on lag putting and 2-putt drills to improve distance control."
    elif total_strokes > benchmarks["Top 100"]["score"]:
        feedback = "Missed greens and penalty strokes likely hurt. Focus on approach consistency and tee shot placement."
    elif total_strokes < benchmarks["Top 10"]["score"]:
        feedback = "Elite scoring — you're trending with the best!"

    return {
        "stats": stats,
        "benchmarks": benchmarks,
        "feedback": feedback
    }
