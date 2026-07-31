## General

The distance condition first determines the entire search interval. Any compatible positive integer must lie from `max(1, n - k)` through `n + k`, inclusive; values below one are excluded because `x` must be positive. This interval contains at most $2k + 1$ integers.

Visit each value in that interval once. Bitwise AND retains a bit only when it is set in both operands, so `(n & value) == 0` is exactly the statement that `n` and `value` have no set-bit position in common. Add the value precisely when this test succeeds.

Every added value is positive, lies within distance `k`, and has disjoint set bits, so every contribution is compatible. Conversely, every compatible integer must be inside the enumerated interval and passes the same bitwise test, so none can be omitted. The accumulated sum is therefore the requested total.

## Complexity detail

The interval contains at most $2k + 1$ candidates, and each uses one constant-time bitwise test. The running time is $O(k)$ and the auxiliary space is $O(1)$; the generator is consumed incrementally rather than stored as a list.

## Alternatives and edge cases

- **Scan from one through `n + k`:** This also finds every compatible value, but it performs $O(n + k)$ checks and wastes work below the lower distance boundary.
- **Bitmask digit DP:** Counts and sums submasks within a numeric interval in logarithmic state depth, but its bookkeeping is unnecessary under the small bounds of this Range I version.
- **Positive lower boundary:** When `n - k <= 0`, enumeration must start at `1`; zero is not a positive compatible integer even though its bitwise AND with `n` is zero.
- **No compatible value:** The running sum naturally remains `0` when every candidate shares at least one set bit with `n`.
- **Inclusive endpoints:** Both `n - k` and `n + k` satisfy the distance bound when positive, so the upper endpoint must be included.
