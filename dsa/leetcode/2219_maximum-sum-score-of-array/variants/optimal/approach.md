## General

**Maintain the two inclusive sums**

Compute the total array sum before the sweep. Immediately before processing an element, `left` is the sum strictly before it and `right` is the sum from that element through the end. Add the current value to `left`; at that moment, `left` is the required inclusive prefix while `right` is the required inclusive suffix.

Compare both values with the best score seen so far, then subtract the current value from `right` before advancing. This update preserves the same interpretation at the next index.

Every index is evaluated exactly once with both sums matching the definition. Taking the maximum across those two values and across all indices therefore examines every candidate sum score. Initializing the answer below the legal numeric range is essential because all candidates may be negative.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. The initial sum and subsequent sweep each take $O(n)$ time.

The algorithm stores only three scalar sums, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Recompute both slices:** Summing the prefix and suffix independently at every index is direct but costs $O(n^2)$ time.
- **Two auxiliary sum arrays:** Prefix and suffix arrays give constant-time scores after preprocessing but use $O(n)$ extra space.
- **All negative values:** The answer must remain negative when every inclusive sum is negative, so zero is not a safe initializer.
- **Single element:** Its prefix and suffix are the same one-element sum.
- **Inclusive overlap:** The current element appears in both candidate sums; neither side should exclude it.
- **Zero values:** They leave running sums unchanged but their indices still need evaluation.
