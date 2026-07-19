## General
**Enumerate indices, not distinct values**

Use three nested loops whose ranges enforce `i < j < k`. This visits each candidate index triple exactly once, which matters when repeated values cause different index choices to produce the same value tuple.

Before entering the innermost loop, test `abs(arr[i] - arr[j]) <= a`. If it fails, no choice of `k` can repair that fixed pair, so skip all extensions of it. Otherwise, test the remaining two differences for every later `k` and increment the answer only when both pass.

**Directly mirror the conjunction**

Every increment corresponds to increasing indices and all three required inequalities, so no invalid triple is counted. Conversely, every good triple appears in the unique iterations matching its three indices, passes the same inequalities, and contributes once. This establishes exact counting without auxiliary sets or value-based deduplication.

The bounds permit at most $\binom{100}{3}=161700$ candidate triples, making direct enumeration appropriate and avoiding a more complicated value-frequency data structure.

## Complexity detail
There are $\binom{n}{3}=O(n^3)$ increasing index triples in the worst case, and each performs constant-time arithmetic. The early pair rejection improves some inputs but does not change the worst-case bound.

Only loop indices, the running count, and temporary differences are stored, giving $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Value-frequency structures:** range-count data structures can reduce asymptotic work, but their bookkeeping is disproportionate for $n\leq100$.
- **Generate combinations:** `itertools.combinations` expresses the same cubic enumeration but does not improve its complexity.
- **Copy data per candidate:** materializing the full input for each triple remains correct but adds an avoidable factor of $n$.
- **Exactly three elements:** there is one candidate, accepted or rejected as a whole.
- **Zero limits:** the relevant pair must contain equal values.
- **Repeated values:** different index triples are counted independently even when their value tuples match.
- **All limits large:** every increasing triple is good, so the result is $\binom{n}{3}$.
- **Boundary equality:** differences equal to their limits qualify because every comparison is inclusive.
