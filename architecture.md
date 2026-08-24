# BONOBO Architecture

## Pipeline

1. Actor/Utility Registry
2. Negotiation Outcome Ingestor
3. Mutual-Gain Analyzer
4. Fairness/Dispersion Engine
5. Exploitative-Gain Detector
6. Trust Update Layer
7. Coalition Stability Monitor
8. Conflict Resolution Scorer
9. Cooperative Optimization Engine
10. Audit Reporter

## Inputs

- actor utilities
- disagreement baselines
- negotiated outcomes
- trust states
- coalition membership
- conflict records
- repeated-round outcomes

## Outputs

```json
{
  "total_gain": 0.62,
  "mutual_gain_fraction": 1.0,
  "fairness_dispersion": 0.03,
  "exploitative_penalty": 0.0,
  "coalition_stability": 0.92,
  "cooperative_optimization": 0.88
}
```

## Design principle

BONOBO distinguishes:
- apparent cooperation
from
- durable mutually beneficial cooperation.

## Integration

ORCA can measure operational coordination.

HORSE can include human actors in mixed negotiations.

TERMITE can study emergent coalition structure.

COBRA can detect divergence between declared cooperative goals and observed behavior.
