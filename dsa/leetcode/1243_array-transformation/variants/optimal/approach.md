## General
**Start with every interior index active.** On the first round, any interior position might be a strict peak or valley. Evaluate all of them against the unchanged current array and collect their signed updates without applying any update early.

**Apply one simultaneous batch.** After every active position has been evaluated, add the collected `+1` or `-1` changes. This preserves the rule that all decisions in a round use the same prior values. The endpoints are never active and therefore never change.

**Restrict the next frontier.** If a position did not change and neither neighbor changed, its complete three-value neighborhood is identical on the next round, so it still cannot change. Consequently, only a changed index and its immediate interior neighbors need reevaluation. Build the next active set from those positions. When a batch contains no updates, the array is stable everywhere: every omitted position has an unchanged neighborhood, and every active position was just shown not to be a strict extremum.

## Complexity detail
The initial frontier contains $O(n)$ indices. Each of the $C$ actual updates contributes at most three positions to the following frontier, so the total number of evaluations is $O(n+C)$. The current array, update batch, and active-index sets use $O(n)$ space.

## Alternatives and edge cases
- **Rescan the full array each round:** It is straightforward and correct but can spend $O(n)$ work per day even when only one local extremum is changing.
- **Update in place during the scan:** This is incorrect because later decisions would observe values from the current round rather than its beginning.
- **Copy the entire array per round:** It preserves simultaneity but still performs unnecessary full-array work on a sparse frontier.
- **Already stable array:** The first evaluation produces no updates and returns the input values unchanged.
- **Equal neighbor:** The comparison is strict; equality with either neighbor prevents an update in that direction.
- **Endpoint:** Positions `0` and `n - 1` remain fixed even if they would be extrema.
- **Direction reversal:** An element may change in different directions on later rounds, so frontier membership—not a permanent per-index direction—is tracked.
