# BONOBO Theory

## 1. Problem

Cooperation can look successful while concealing:
- unequal benefit,
- unstable compromise,
- hidden coercion,
- repeated defection,
- coalition fragility,
- short-term gains that damage long-term trust.

BONOBO evaluates whether cooperative behavior is durable and mutually beneficial.

## 2. Actor utilities

Let actors be:

`A = {a_1, ..., a_n}`

Each actor has utility:

`U_i(o)`

for negotiated outcome `o`.

## 3. Mutual gain

Relative to disagreement baseline `U_i^0`:

`G_i = U_i(o) - U_i^0`

A cooperative outcome should ideally satisfy:

`G_i >= 0`

for all materially participating actors.

## 4. Aggregate gain

`G_total = sum_i G_i`

But total gain alone is insufficient.

A highly unequal outcome may maximize total gain while destabilizing the coalition.

## 5. Fairness dispersion

Let gains be normalized:

`g_i = G_i / (sum_j |G_j| + eps)`

Candidate dispersion:

`F = variance(g_i)`

Lower dispersion suggests more balanced benefit.

## 6. Exploitative gain penalty

If any actor's gain is strongly negative while others benefit:

`E = sum_i max(0, -G_i)`

This explicitly penalizes extraction hidden inside aggregate optimization.

## 7. Negotiation efficiency

If best known achievable total gain is `G*`:

`N = G_total / (G* + eps)`

## 8. Coalition stability

Run repeated rounds with updated trust and incentives.

Let coalition remain intact over `T` rounds.

`S = stable_rounds / T`

## 9. Trust update

For actor pair `(i,j)`:

`T_ij(t+1) = lambda*T_ij(t) + (1-lambda)*observed_reliability_ij(t)`

Repeated promise violation should reduce trust.

## 10. Cooperative optimization score

Candidate score:

`C = w1*N + w2*S + w3*(1-F) - w4*E + w5*resolution_quality`

after normalization.

## 11. EFMW interpretation

The EFMW-inspired element is recursive relational evaluation across:
- utilities,
- promises,
- trust,
- coalitions,
- outcomes,
- conflict history.

## 12. Falsifiable prediction

BONOBO should add value when:
- utility is multi-party,
- cooperation unfolds over time,
- trust updates matter,
- total welfare can hide unequal harm.

If standard bargaining and multi-agent cooperation metrics capture the same outcomes, BONOBO adds no justified complexity.
