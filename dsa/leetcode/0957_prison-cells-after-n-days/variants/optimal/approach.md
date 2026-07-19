## General
**Compute one day from the old state only.** Construct a fresh eight-value list whose endpoints are zero. For each interior index, write `1` exactly when its left and right neighbors in the previous state are equal. A fresh list preserves the required simultaneous-update semantics.

**Detect repetition instead of simulating every day.** An eight-cell binary row has only $2^8=256$ possible states. Record each state together with the number of days still remaining when it is encountered. If the same state appears again, the intervening sequence is a cycle; the difference between the two remaining-day counts is its length.

**Skip complete cycles.** Replace the remaining day count by its remainder modulo the cycle length. Whole cycles would return to the same state and therefore cannot affect the final answer. Simulate only the remaining fraction of a cycle. This preserves the exact day requested because the skipped updates comprise an integer number of identical state cycles.

The process is deterministic, so once a state repeats, every later state repeats in the same order. The returned state is consequently identical to a direct `n`-day simulation, while the number of states actually examined is bounded by the fixed state space rather than by `n`.

## Complexity detail
At most 256 distinct states can be visited before a repetition, and each update examines exactly eight cells. Both time and stored state count are bounded by constants independent of `n`, giving $O(1)$ time and $O(1)$ space for the fixed eight-cell contract.

## Alternatives and edge cases
- **Direct day-by-day simulation:** Apply the transition exactly `n` times. It is correct but costs $O(n)$ time and is infeasible when `n` approaches $10^9$.
- **Use the known 14-day period:** States after the first update follow a period dividing 14. Hard-coding that fact is compact, but generic cycle detection derives the period and is less error-prone.
- **In-place left-to-right update:** Mutating cells while computing the same day incorrectly lets later cells observe already-updated neighbors.
- **Endpoints:** Positions zero and seven always become zero because they do not have two adjacent neighbors.
- **All vacant:** Interior cells become occupied on the next day because their two neighbors are equal.
- **Large day count:** Cycle reduction must occur before attempting a direct loop over all remaining days.
