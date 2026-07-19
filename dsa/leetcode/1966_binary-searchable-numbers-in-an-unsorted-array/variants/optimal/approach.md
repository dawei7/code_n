## General
**Characterize a guaranteed target**

Suppose the target is `nums[i]`. If an earlier pivot is larger than the
target, the process removes that pivot and everything to its right, including
the target. Therefore every value left of `i` must be smaller than
`nums[i]`.

Symmetrically, if a later pivot is smaller than the target, removing that pivot
and everything to its left discards the target. Every value right of `i` must
therefore be larger. These conditions are also sufficient: every non-target
pivot then removes only elements on its own side of the target, so the target
remains until it is selected.

**Check both sides in constant time**

Build `suffix_minimum[i]`, the smallest value from index `i` onward. During a
left-to-right scan, retain the largest value already passed. Position `i` is
counted exactly when

$$
\max(\text{values left of }i)
<
\texttt{nums[i]}
<
\min(\text{values right of }i).
$$

Use negative and positive infinity for the empty side at either endpoint.
Uniqueness makes the strict inequalities match the contract directly.

## Complexity detail
Building suffix minima and scanning with a prefix maximum each take $O(N)$
time. The suffix array stores $N+1$ values, using $O(N)$ auxiliary space.

## Alternatives and edge cases
- **Inspect both sides for every index:** Directly test all earlier and later
  values. This follows the characterization but takes $O(N^2)$ time.
- **Sort values with their indices:** A value qualifies when all smaller values
  occur before it and all larger values occur after it, but sorting raises the
  time to $O(N\log N)$.
- A one-element array always contributes one searchable value.
- Every element of a strictly increasing array qualifies.
- No element of a strictly decreasing array of length greater than one
  qualifies.
- The first and last positions have one empty side, handled by the infinity
  sentinels.
