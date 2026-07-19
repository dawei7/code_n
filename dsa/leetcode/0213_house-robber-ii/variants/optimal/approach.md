## General
The circular street differs from the linear problem in exactly one conflict: houses `0` and $n - 1$ are adjacent. Any valid selection must exclude at least one of them. Split the solution space into two exhaustive linear cases:

- Rob only among houses $0 .. n - 2$, excluding the last.
- Rob only among houses $1 .. n - 1$, excluding the first.

For either range, use the linear take-or-skip recurrence. At each amount, keep the better of the previous prefix optimum and the optimum two positions back plus the current amount. Two rolling values are sufficient.

For `[1,2,3,1]`, the first range `[1,2,3]` has optimum `4`, while the second `[2,3,1]` has optimum `3`; their maximum is `4`. For `[2,3,2]`, both endpoint-excluding ranges have optimum `3`, preventing the illegal choice of both `2`s.

The single-house case must be handled before forming the two ranges. That one house is adjacent only to itself conceptually, but it may be robbed once and should return its value.

Every valid circular selection excludes the first house or excludes the last house (possibly both), so it belongs to at least one of the two linear cases. The linear recurrence exhaustively compares selections that omit each current house with those that include it and therefore solves each case optimally. Taking the larger case optimum considers every circularly valid selection and introduces none that contains both endpoints. The result is thus globally optimal.

## Complexity detail
Each linear helper scans at most $n - 1$ houses, so two passes take $O(n)$ time. Rolling prefix values use $O(1)$ auxiliary space; avoid materializing slices if strict constant space is required.

## Alternatives and edge cases
- Running the linear recurrence once over the full array can illegally select both endpoints.
- Full DP arrays are correct but use $O(n)$ space instead of rolling state.
- Greedily selecting the largest remaining house can block a better combination.
- One house returns its value; two houses return the larger value.
- Zero-valued houses do not affect the optimum.
