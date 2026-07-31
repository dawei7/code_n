## General

An original value `v` can become an integer target `x` exactly when $v-k \le x \le v+k$. Treat this inclusive range as an interval contributed by that array position. Let $R(x)$ be the number of intervals covering `x`, and let $C(x)$ be the number of elements already equal to `x`.

The $C(x)$ existing copies need no changes. Among the other $R(x)-C(x)$ reachable elements, at most `numOperations` can be selected and changed to `x`. Thus the best frequency for a fixed target is

$$
C(x)+\min(\texttt{numOperations},R(x)-C(x)).
$$

Perform a difference-event sweep. Every interval `[v - k, v + k]` adds one at `v - k` and removes one at `v + k + 1`; applying all events at a coordinate gives the inclusive coverage there. Also insert every original value as a zero-delta event so the sweep evaluates each coordinate where $C(x)$ can be positive.

No other coordinates are needed. Between event coordinates, $R(x)$ is constant, so an absent target has the same score throughout that segment and its left boundary is evaluated. At an original value, the additional unchanged copies are handled explicitly. Taking the largest score over the sweep therefore considers every possible optimum.

Although the contract requires exactly `numOperations` selections, the calculation may use fewer productive changes. Any remaining selections can add zero to previously unselected indices, which is always permitted and does not reduce the achieved frequency.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. There are $O(n)$ interval endpoints and original-value coordinates. Building them takes $O(n)$ time, sorting them takes $O(n\log n)$ time, and the sweep is linear. The total is $O(n\log n)$ time and $O(n)$ auxiliary space.

The benchmark size is $n$. Its increasing consecutive arrays create $O(n)$ distinct events. The calibrated slower method evaluates the same complete set of candidate targets but scans all $n$ values separately for each target, requiring $O(n^2)$ time.

## Alternatives and edge cases

- **Sort plus binary searches:** For every original target, two searches can count values in its reachable range, but absent targets still require separate handling.
- **Scan every target and every element:** This is straightforward and correct over the bounded coordinate range, but takes $O(n^2)$ work on the benchmark's distinct candidates.
- **Coordinate-sized difference array:** Values are bounded, so a dense array can work, but the sparse event map avoids dependence on the numeric coordinate span.
- **Best target absent from `nums`:** Interval boundaries must be evaluated; checking only original values misses cases such as `[1, 5]` with `k = 2`.
- **Existing duplicates:** Copies already equal to the target do not consume operation budget.
- **Zero `k`:** Every reachability interval is a single point, so no frequency can exceed its original count.
- **Exact operations:** Adding zero lets surplus required operations act as no-ops on distinct unused indices.
