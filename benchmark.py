from bonobo import BonoboEvaluator

baselines = {
    "A":0.4,
    "B":0.4,
    "C":0.4
}

balanced = {
    "A":0.70,
    "B":0.68,
    "C":0.66
}

exploitative = {
    "A":0.95,
    "B":0.72,
    "C":0.20
}

if __name__ == "__main__":
    ev = BonoboEvaluator(baselines)
    print("balanced", ev.evaluate(
        balanced,
        best_known_total_gain=0.9,
        coalition_stability=0.95,
        resolution_quality=0.9
    ))
    print("exploitative", ev.evaluate(
        exploitative,
        best_known_total_gain=0.9,
        coalition_stability=0.55,
        resolution_quality=0.5
    ))
