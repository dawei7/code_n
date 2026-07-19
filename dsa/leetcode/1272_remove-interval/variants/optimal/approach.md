## General
**Classify each interval against the removal range**

Process the already sorted input from left to right. For an interval `[start, end]`, there is no overlap when `end <= remove_start` or `start >= remove_end`. The non-strict comparisons are essential for half-open intervals: touching at either endpoint removes no real numbers. Append such an interval unchanged.

When the intervals overlap, preserve a left piece `[start, remove_start]` exactly when `start < remove_start`. Preserve a right piece `[remove_end, end]` exactly when `end > remove_end`. These strict tests prevent empty intervals. If neither condition holds, the input interval lies wholly inside the removal interval and contributes nothing. If both hold, the removal interval sits strictly inside the input and splits it into two pieces.

For every input interval, these retained pieces are exactly the points outside the removal range, so their union is the required set difference. Processing inputs in their original order and emitting each left piece before its right piece preserves sorted order. Subtracting points cannot create overlap between intervals that were initially disjoint.

## Complexity detail
Each of the $n$ intervals is examined once and emits at most two pieces, so the running time is $O(n)$. The returned list can contain up to $n+1$ intervals and therefore uses $O(n)$ space; excluding the required output, the sweep uses $O(1)$ auxiliary state.

## Alternatives and edge cases
- **Front insertion followed by reversal:** It can preserve the same final order, but repeatedly shifting an expanding list takes $O(n^2)$ time.
- **Endpoint-event sweep:** Treating all endpoints as events generalizes to many set operations but adds sorting and bookkeeping that the sorted disjoint input does not need.
- **Complete coverage:** An interval entirely inside `to_be_removed` emits no piece.
- **Removal strictly inside one interval:** Both residual sides are nonempty and must be emitted.
- **Touching endpoints:** `[a,b)` and `[b,c)` do not overlap, so the original interval remains unchanged.
- **Removal outside the represented set:** Every interval is copied unchanged.
- **Negative coordinates:** Comparisons work identically across zero; no special arithmetic is required.
