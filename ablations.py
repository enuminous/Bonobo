from bonobo import BonoboEvaluator
from benchmark import baselines, exploitative

if __name__ == "__main__":
    ev = BonoboEvaluator(baselines)
    out = ev.evaluate(
        exploitative,
        best_known_total_gain=0.9,
        coalition_stability=0.55,
        resolution_quality=0.5
    )
    print("full cooperative score:", out["cooperative_optimization"])
    print("total gain only:", out["total_gain"])
