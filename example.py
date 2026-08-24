from bonobo import BonoboEvaluator

baselines = {
    "planner":0.5,
    "executor":0.5,
    "reviewer":0.5
}

outcome = {
    "planner":0.72,
    "executor":0.69,
    "reviewer":0.67
}

print(BonoboEvaluator(baselines).evaluate(
    outcome,
    best_known_total_gain=0.7,
    coalition_stability=0.9,
    resolution_quality=0.85
))
