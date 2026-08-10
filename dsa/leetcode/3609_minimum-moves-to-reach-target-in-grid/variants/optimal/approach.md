## General

Forward moves only increase coordinates, and a target can grow very large. Searching outward from the start would create branching paths and may explore many useless states. The source instead works backward from `(tx, ty)`. Away from equality, the relative sizes of the target coordinates determine which coordinate the last forward move must have changed, and its predecessor can be reconstructed directly.

Each successful reverse step corresponds to exactly one forward move, so the number of reverse steps is the required minimum when the start is reached.

**Why the larger coordinate identifies the last move**

Suppose the current reverse state has `tx > ty`. The last forward move could not have increased the y-coordinate. A forward y-move from `(x,y)` produces:

`(x, y + max(x,y))`,

whose new y-coordinate is at least `x`. Such a result cannot have x strictly larger than y. Therefore, the last move must have increased x, while y remained `ty`.

The argument is symmetric when `ty > tx`: the last move must have increased y.

**Reversing an x-increase**

Let the predecessor be `(x, ty)` and the current larger coordinate be:

`tx = x + max(x, ty)`.

There are two cases.

If `x >= ty`, the maximum was x, so `tx = 2x`. The predecessor is `x = tx / 2`, which requires `tx` to be even. This case produces `tx >= 2ty`.

If `x < ty`, the maximum was `ty`, so `tx = x + ty`. The predecessor is `x = tx - ty`, and the resulting current ratio satisfies `ty < tx < 2ty`.

At the boundary `tx = 2ty`, subtraction gives predecessor `x = ty`, which is valid because `max(x,ty)=ty`. The source therefore uses:

- when `tx > 2 * ty`, require an even `tx` and halve it;
- otherwise, subtract `ty` from `tx`.

The y-larger branch applies the identical rules with the coordinates exchanged.

**Why an odd value above twice the other is impossible**

When `tx > 2ty`, the subtraction predecessor `tx - ty` would still be greater than `ty`. If that predecessor were larger, the forward maximum would have been the predecessor itself, so the move should have doubled it rather than added `ty`. The only valid predecessor is `tx / 2`.

If `tx` is odd, no integer predecessor can double to it. The source immediately returns `-1`. The same reasoning handles odd `ty > 2tx`.

**The special equality state**

When `tx == ty == z > 0`, the preceding state must have one zero coordinate.

For example, if the last move increased x from `(x,z)`, then:

`x + max(x,z) = z`.

The maximum is at least z, so the only solution is `x = 0`. The predecessor is `(0,z)`. Similarly, if the last move increased y, the predecessor is `(z,0)`.

The source decides which predecessor can still reach the given start:

- if `sy == 0`, it sets `ty = 0`, choosing predecessor `(z,0)`;
- otherwise, if `sx == 0`, it sets `tx = 0`, choosing `(0,z)`;
- if neither start coordinate is zero, equality cannot be reversed toward that start and the answer is `-1`.

Forward moves never decrease a coordinate. Therefore, a reverse path toward a start with positive `sy` must never reduce y to zero, and similarly for x. The start's zero coordinate resolves the only apparent two-way ambiguity.

The check `if tx == 0: return -1` protects the all-zero equality case inside the loop. Under the stated ordering `sx <= tx` and `sy <= ty`, target `(0,0)` can only pair with start `(0,0)` and normally exits before the loop, but the guard makes the reverse rule explicit.

**Preventing overshoot past the start**

The loop continues while either target coordinate is still greater than its corresponding start coordinate. At the beginning of each iteration, it checks whether `tx < sx` or `ty < sy`. Once a reverse step drops below a start coordinate, forward moves—which only increase coordinates—cannot repair that mismatch while still reproducing the unique reverse history. The target is unreachable.

After the loop, the code returns `moves` only if both coordinates exactly equal the start. This final equality check rejects any state where one loop condition ended without a complete match.

**Following the first example backward**

Start is `(1,2)` and target is `(5,4)`.

At `(5,4)`, x is larger but not greater than `2*4`, so the subtraction case gives `(1,4)`. This reverses the forward move that added maximum 4 to x.

At `(1,4)`, y is greater than `2*1` and is even, so it is halved to 2, giving `(1,2)`. This reverses doubling y from 2 to 4 because y was the maximum at the predecessor.

The start is reached in two reverse steps, matching the two forward moves.

**Why the reconstructed path is minimal**

Whenever coordinates are unequal, the larger coordinate proves which coordinate changed last. Its ratio to the smaller coordinate then determines whether the predecessor came from doubling or addition; the parity check determines whether that predecessor exists. At equality, only the zero-coordinate predecessors are possible, and the start constraints select the viable one.

Thus there is no alternative last move that could skip a reverse step or produce a shorter route. Every accepted reverse transformation is the inverse of one legal forward move, and every legal path to the current state must end with that transformation. Inductively, reaching the start after `moves` steps produces a valid path and no path can use fewer moves.

**Why the loop is logarithmic**

If the larger coordinate is more than twice the smaller one, it is halved. Otherwise, subtraction makes the old smaller coordinate the new maximum, and the old larger coordinate was at most twice that value. In either case, the maximum coordinate drops to at most about half its previous scale after the reverse step. Equality also introduces a zero and subsequent valid steps use halving behavior.

Consequently, the numeric magnitude shrinks geometrically rather than by repeated subtraction of a tiny fixed value.

## Complexity detail

Let `M = \max(tx,ty)` for the original target. Each iteration performs constant-time comparisons and arithmetic and reduces the scale of the larger coordinate geometrically. The number of iterations is `O(\log M)`.

Only `moves` and the four coordinate variables are stored. The algorithm is iterative and allocates no visited set or recursion stack, so auxiliary space is `O(1)`.

Python integers represent values through `10^9` exactly, and all arithmetic stays within that range while reversing.

## Alternatives and edge cases

- **Forward breadth-first search:** It branches twice per state and is impractical on an unbounded grid with coordinates up to `10^9`.
- **Memoized forward recursion:** It still explores branching states and offers no advantage over the forced reverse predecessor.
- **Subtract repeatedly like the Euclidean algorithm:** The move rule sometimes doubles the current maximum; the ratio test and halving step are necessary to invert it correctly.
- **Start already equals target:** The loop does not run and the answer is 0.
- **Target coordinate below start:** The constraints exclude this initially, while the in-loop check rejects it if reverse processing overshoots.
- **Larger coordinate above twice the other and odd:** No integer doubling predecessor exists, so the target is unreachable.
- **Larger coordinate exactly twice the other:** The subtraction branch yields equal predecessor coordinates and represents a valid move.
- **Positive equal target coordinates:** The only predecessors have one coordinate zero.
- **Neither start coordinate is zero at equality:** No reverse path can reach that start, so the result is `-1`.
- **One start coordinate is zero:** It selects the corresponding equality predecessor without guessing.
- **Start `(0,0)` and positive target:** The forward maximum is always zero at the origin, so no move changes the point; reverse processing ultimately rejects the target.
- **Example `(1,1) -> (2,2)`:** Equality at the target requires a zero-coordinate predecessor, incompatible with the positive start, so the answer is `-1`.
- **Coordinates on an axis:** The nonzero coordinate can only double until the other coordinate becomes positive through a move that adds the maximum.
- **No mutation of caller data:** All parameters are immutable integers; the source rebinds local `tx` and `ty` only.
