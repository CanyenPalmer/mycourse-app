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

    # PGA Benchmarks (example values)
    benchmarks = {
        "Top 100": {"score": total_par + 3, "putts": 32},
        "Top 50": {"score": total_par + 1, "putts": 30},
        "Top 10": {"score": total_par - 1, "putts": 28},
    }

    feedback = "Great round! Keep improving."

    if total_putts > benchmarks["Top 100"]["putts"]:
        feedback = "Less 3 putts! Work on distance control drills with lag putting."
    elif total_strokes > benchmarks["Top 100"]["score"]:
        feedback = "Focus on tee shots and avoiding penalties for lower scores."

    return {
        "stats": stats,
        "benchmarks": benchmarks,
        "feedback": feedback
    }
