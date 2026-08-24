import unittest
from bonobo import BonoboEvaluator

class TestBonobo(unittest.TestCase):
    def test_mutual_gain_fraction(self):
        ev = BonoboEvaluator({"A":0.5,"B":0.5})
        out = ev.evaluate({"A":0.7,"B":0.6})
        self.assertEqual(out["mutual_gain_fraction"],1.0)

    def test_exploitation_detected(self):
        ev = BonoboEvaluator({"A":0.5,"B":0.5})
        out = ev.evaluate({"A":0.9,"B":0.2})
        self.assertGreater(out["exploitation_penalty"],0.0)

    def test_balanced_beats_exploitative(self):
        ev = BonoboEvaluator({"A":0.4,"B":0.4,"C":0.4})
        good = ev.evaluate(
            {"A":0.7,"B":0.68,"C":0.66},
            best_known_total_gain=0.9,
            coalition_stability=0.95,
            resolution_quality=0.9
        )
        bad = ev.evaluate(
            {"A":0.95,"B":0.72,"C":0.2},
            best_known_total_gain=0.9,
            coalition_stability=0.55,
            resolution_quality=0.5
        )
        self.assertGreater(good["cooperative_optimization"], bad["cooperative_optimization"])

if __name__ == "__main__":
    unittest.main()
