# Cooperation Model

## Actor schema

```json
{
  "id": "agent-A",
  "baseline_utility": 0.40,
  "trust": {
    "agent-B": 0.75
  }
}
```

## Outcome schema

```json
{
  "utilities": {
    "agent-A": 0.70,
    "agent-B": 0.66,
    "agent-C": 0.61
  }
}
```

## Gain

`G_i = outcome_utility_i - baseline_utility_i`

## Exploitation signal

A candidate exploitation signal is present when:
- total gain is positive,
- at least one participating actor has a large negative gain.

## Coalition stability

Track:
- membership changes
- repeated defections
- renegotiation frequency
- broken commitments

## Conflict resolution

Resolution quality should include:
- whether the conflict was actually resolved,
- whether the same conflict reappears,
- whether the resolution worsened another actor's position.
