## General

**Use symmetry to consider only a positive target**

Every sequence of left and right moves reaching a positive position can be mirrored by reversing every direction, reaching the corresponding negative position in the same number of moves. Therefore only the magnitude matters, and the solution replaces `target` with `abs(target)`.

**Start by imagining every move goes right**

After `k` moves, if all moves go right, the position is the triangular sum

`s = 1 + 2 + ... + k = k(k + 1) / 2`.

Changing move `i` from right to left changes its contribution from `+i` to `-i`. The final position decreases by `2i`.

If a set of moves with total length `q` is reversed, the final position becomes

`s - 2q`.

Thus target is reachable in exactly `k` moves if and only if:

- `s >= target`, so the required decrease is nonnegative.
- `s - target` is even, so it can equal `2q`.

**Why the parity condition is also sufficient**

When `s - target` is even, define `q = (s - target) / 2`. We need a subset of move lengths `1, 2, ..., k` summing to `q`.

Every integer from zero through `s` can be formed from these consecutive lengths. This can be proved inductively: after lengths through `r - 1` form every value through their sum, adding `r` extends coverage without a gap because `r` is at most one more than the previous total. Therefore such a subset exists whenever `0 <= q <= s`.

Reversing that subset reaches the target.

**Search the first feasible move count**

The solution maintains current move count `k` and all-right sum `s`. It first tests feasibility, then increments `k` and adds the new move length to `s`.

The first satisfying `k` is minimal because every smaller move count was tested and failed either to reach the target magnitude or to have compatible parity.

**Trace target two**

- With zero moves, `s = 0` is too small.
- After one move, `s = 1` is too small.
- After two moves, `s = 3` is large enough, but `3 - 2 = 1` is odd.
- After three moves, `s = 6` and `6 - 2 = 4` is even.

Reverse moves totaling two, namely move two. The signed moves are `+1, -2, +3`, which finish at two.

**Why overshooting is useful**

The process does not need to land on the target using all-right moves. Overshooting creates an amount that can be removed in even increments by flipping directions. Only magnitude and parity determine whether the overshoot can be corrected.

For example, target four is not a triangular sum. After three moves the all-right position is six, and the difference is two. Reversing move one subtracts two, producing four. The ability to change signs turns many overshoots into exact solutions.

**The variables mirror the mathematical state**

Before each feasibility check, `k` is the number of moves already included and `s` is their triangular sum. The update first increases `k` and then adds that new length to `s`, preserving `s = k(k + 1) / 2` for the next check.

**Why the loop must eventually terminate**

Triangular sums grow without bound, so `s` eventually exceeds the target. Their parity changes in a repeating pattern as successive `k` values are added. If the first crossing has the wrong parity, one or two additional moves produce a compatible difference. A feasible state therefore always appears.


For each `k`, the feasibility test is necessary because direction reversals change the all-right sum only by a nonnegative even value. It is sufficient because the required half-difference can be formed from a subset of move lengths.

The loop returns the first feasible `k`, so the result is both reachable and minimal.

## Complexity detail

The loop stops when a triangular sum near `target` is reached. Solving `k(k + 1) / 2 >= |target|` shows `k = O(sqrt(|target|))`. Each iteration is constant time, so the exact implementation takes `O(sqrt(|target|))` time and `O(1)` space.

The manifest’s `O(1)` description would correspond to a closed-form square-root estimate followed by a constant number of parity adjustments under a unit-cost arithmetic model. The stored source explicitly loops through all move counts and therefore has the square-root bound.

## Alternatives and edge cases

- **Closed-form starting estimate:** Use the quadratic formula to jump to the smallest triangular sum at least the target, then add moves until parity matches. This reduces the loop to a constant number of adjustments.

- **Breadth-first search over positions:** It finds the minimum but the reachable position range grows quickly and wastes memory on states summarized by the parity argument.

- **Require exact triangular equality:** This misses valid solutions that overshoot and flip some move directions.

- **Negative target:** Absolute value is safe because every route can be mirrored.

- **Wrong-parity first crossing:** Continue adding moves; a larger triangular sum can make the difference even.

- **Target is nonzero:** The contract excludes zero, though the loop would correctly return zero moves for it.

- **Large magnitude:** The number of iterations grows only with the square root, not linearly with the target.
