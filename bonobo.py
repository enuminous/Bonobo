from dataclasses import dataclass
from typing import Dict, List, Optional
from statistics import mean, variance

@dataclass
class BonoboConfig:
    w_efficiency: float = 0.30
    w_stability: float = 0.25
    w_fairness: float = 0.20
    w_exploitation: float = 0.15
    w_resolution: float = 0.10

class BonoboEvaluator:
    def __init__(self, baselines: Dict[str,float], config: Optional[BonoboConfig]=None):
        self.baselines = baselines
        self.config = config or BonoboConfig()

    @staticmethod
    def clip01(x):
        return max(0.0, min(1.0, float(x)))

    def evaluate(
        self,
        utilities: Dict[str,float],
        best_known_total_gain: Optional[float] = None,
        coalition_stability: float = 1.0,
        resolution_quality: float = 1.0
    ):
        gains = {}
        for actor, base in self.baselines.items():
            if actor in utilities:
                gains[actor] = utilities[actor] - base

        total_gain = sum(gains.values())
        mutual_fraction = (
            sum(1 for g in gains.values() if g >= 0) / len(gains)
            if gains else 0.0
        )

        abs_total = sum(abs(g) for g in gains.values()) or 1.0
        norm = [g/abs_total for g in gains.values()]
        fairness_dispersion = variance(norm) if len(norm) > 1 else 0.0

        exploitation = sum(max(0.0,-g) for g in gains.values())

        if best_known_total_gain is None or best_known_total_gain <= 0:
            efficiency = 1.0 if total_gain >= 0 else 0.0
        else:
            efficiency = self.clip01(total_gain/best_known_total_gain)

        fairness_score = 1.0/(1.0 + fairness_dispersion)
        exploit_penalty = self.clip01(exploitation)

        coop = (
            self.config.w_efficiency*efficiency +
            self.config.w_stability*self.clip01(coalition_stability) +
            self.config.w_fairness*fairness_score +
            self.config.w_exploitation*(1.0-exploit_penalty) +
            self.config.w_resolution*self.clip01(resolution_quality)
        )

        return {
            "gains": gains,
            "total_gain": total_gain,
            "mutual_gain_fraction": mutual_fraction,
            "fairness_dispersion": fairness_dispersion,
            "exploitation_penalty": exploit_penalty,
            "efficiency": efficiency,
            "coalition_stability": coalition_stability,
            "resolution_quality": resolution_quality,
            "cooperative_optimization": self.clip01(coop)
        }
