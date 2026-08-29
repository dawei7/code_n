## General

**Respect the index order while compressing the choices.** A triplet has value

$$
(\texttt{nums[i]}-\texttt{nums[j]})\cdot\texttt{nums[k]}
$$

with $i<j<k$. Trying all triples repeats the same questions. Before choosing `j`, only the greatest earlier `nums[i]` matters because all values are positive: for a fixed `j`, larger `nums[i]` produces a larger difference. Before choosing `k`, only the greatest difference formed by an earlier ordered pair $(i,j)$ matters because multiplying by positive `nums[k]` preserves order.

The source compresses those two layers into scalar variables:

- `mx` is the largest array value among indices already passed, available as a future first element;
- `mx_diff` is the largest non-negative value `nums[i] - nums[j]` from an ordered pair entirely before the current position;
- `ans` is the largest complete triplet value formed so far.

**One element plays three possible roles in a precise order.** For each current value `x`, the code performs:

`ans = max(ans, mx_diff * x)`

`mx_diff = max(mx_diff, mx - x)`

`mx = max(mx, x)`

The order of these statements is the core of the solution.

First, current `x` is treated as `nums[k]`. At this moment `mx_diff` contains only pairs whose two indices are earlier, so multiplying them by `x` respects $i<j<k$.

Second, current `x` is treated as `nums[j]`. The current `mx` still contains only values at earlier indices, so `mx - x` represents a legal ordered difference with $i<j$. That difference becomes available only for later values of `k`.

Third, current `x` is admitted into `mx` as a possible `nums[i]` for future middle indices. Updating `mx` earlier would allow one index to serve simultaneously as both `i` and `j`, while updating `mx_diff` before `ans` would allow current index to serve as both `j` and `k`. The source's order prevents both errors without storing indices.

**Why zero initialization is correct.** All `nums` values are positive. A negative difference multiplied by a positive final value is negative, and the problem says to return zero if no positive triplet value exists. Therefore negative differences never need to be retained. Initializing `mx_diff = 0` means “use no profitable pair yet,” and initializing `ans = 0` implements the required floor at zero.

Similarly, `mx = 0` is below every legal positive array value. During the first iteration it produces a non-positive candidate difference that does not replace `mx_diff`, then it becomes the actual first value.

**Deriving the invariant.** Just before processing index $p$:

$$
\texttt{mx}
=
\max_{0\le i<p}\texttt{nums[i]},
$$

and

$$
\texttt{mx\_diff}
=
\max\left(
0,\
\max_{0\le i<j<p}
(\texttt{nums[i]}-\texttt{nums[j]})
\right).
$$

The first statement uses the best legal difference with current index as $k$. The second extends the pair invariant with current index as $j$, using the best earlier first value. The third extends the prefix maximum invariant. Induction over the scan proves those meanings remain true.

For every possible $k$, `mx_diff * nums[k]` is the best triplet ending exactly at that $k$. Taking the maximum over all scan positions therefore considers the best triplet for every final index and yields the global optimum.

**Trace `[12,6,1,2,7]`.** After seeing `12` then `6`, the best difference becomes `12 - 6 = 6`. At `1` it becomes `12 - 1 = 11`. When `7` is processed as the final multiplier, `ans` considers `11 * 7 = 77`. Only after that does `7` affect pair state, so the winning indices remain ordered $(0,2,4)$.

Although this first version permits only `n <= 100` and brute force could pass, the checked-in solution is the fully optimized one-pass method. It is also the same idea needed by the larger follow-up version.

## Complexity detail

The loop examines each of $n$ values once and performs a constant number of arithmetic and maximum operations, so time is $O(n)$. Only three scalar state variables and the current loop value are stored, giving $O(1)$ auxiliary space. The input is not modified.

The product can be as large as roughly $10^{12}$ because values reach $10^6$. Python integers are safe; fixed-width implementations need a 64-bit integer for differences, multiplication, and the answer. The manifest's $O(n)$ time and $O(1)$ space match the exact implementation.

## Alternatives and edge cases

- **Triple enumeration:** Three nested loops directly evaluate every triplet in $O(n^3)$ time. It fits the small first-version constraint but hides the reusable optimization.
- **Fix `j` and `k`:** Track the greatest prefix value for `i` inside two loops, reducing time to $O(n^2)$ and constant space.
- **Prefix and suffix maxima:** For each middle index, combine the greatest left value and greatest right multiplier in $O(n)$ time but $O(n)$ extra space.
- **Strictly increasing array:** Every ordered difference `nums[i] - nums[j]` is negative, so `mx_diff` stays zero and the result is zero.
- **Duplicate values:** Equal endpoints create difference zero, which is harmless and may remain as the best non-negative difference until a positive one appears.
- **Update order:** Evaluate answer, then pair difference, then prefix maximum. Changing this sequence can reuse the current index in multiple triplet positions.
- **Exactly three elements:** The scan still evaluates their sole legal ordered triplet and clamps a negative value to zero.
- **Positive-value guarantee:** It justifies keeping only the maximum difference. With negative multipliers, the minimum difference could also matter.
