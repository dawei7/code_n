## General

**A restriction affects every building, not only its own index.** If building `i` has height at most `h` and adjacent heights may differ by at most one, then building `j` can be at most `h + abs(j - i)`. A low restriction creates a cone-shaped upper bound spreading left and right. The true limit at any position is the minimum of all such propagated bounds.

The number of buildings can be one billion, so calculating a limit for every index is impossible. The solution works only with explicitly restricted positions plus two boundary anchors. Between consecutive anchors, the maximum possible shape is determined mathematically.

**Add the fixed first building.** The code aliases the input with `r = restrictions` and appends `[1, 0]`, representing the rule that building one must have height zero. It then sorts `r` by building index.

This is not a copy: appending and sorting mutate the caller’s `restrictions` list. Later propagation also lowers some stored maximum heights in place. That mutation is part of the exact implementation behavior.

**Represent the unrestricted right boundary.** If no explicit restriction exists at building `n`, the method appends `[n, n - 1]`. Starting from height zero at building one and rising by at most one per step, building `n` can never exceed `n - 1`, so this anchor adds no artificial restriction. It merely closes the final interval so its possible peak is evaluated. Because the list was already sorted and `n` is the greatest index, appending this final anchor preserves order.

If building `n` already has an explicit restriction, no default anchor is appended. That existing row closes the final interval instead.

**Propagate bounds from left to right.** For adjacent restricted rows at indices `x` and `y` with `x < y`, a left height limit `h_x` implies `h_y <= h_x + y - x`. The first pass applies

`r[i][1] = min(r[i][1], r[i - 1][1] + r[i][0] - r[i - 1][0])`.

After this pass, each stored height respects every restriction to its left. The minimum preserves a tighter original limit rather than loosening it.

**Propagate bounds from right to left.** A restriction at `y` similarly implies `h_x <= h_y + y - x`. The backward pass lowers each interior stored height against its right neighbor’s propagated bound. It iterates down to index one and deliberately does not rewrite the anchor at list index zero, whose fixed building-one height is already zero and cannot be lowered.

After both passes, every stored height is the tightest upper bound at that restricted index induced by restrictions on both sides. In particular, consecutive adjusted limits are mutually reachable: their difference cannot exceed the distance between their building indices.

**Find the highest integer peak between two limits.** Consider consecutive anchors `(x, h_x)` and `(y, h_y)` with distance `d = y - x`. Starting from the left, height can rise at slope one, giving bound `h_x + p` after `p` steps. Starting from the right, it is bounded by `h_y + d - p`. The realizable upper envelope at that position is the smaller of those two values.

The two lines meet near the interval’s maximum. If a peak has height `H`, climbing from the left limit needs at least `H - h_x` steps and descending to the right limit needs at least `H - h_y` steps. Their sum cannot exceed `d`:

`(H - h_x) + (H - h_y) <= d`.

Solving gives

`H <= (h_x + h_y + d) / 2`.

Heights must be integers, so the greatest possible peak is

`floor((h_x + h_y + d) / 2)`.

The final loop calculates exactly this value as `t` for every adjacent pair and keeps the maximum in `ans`.

**Why the formula remains valid when one endpoint is much higher.** The propagation passes guarantee `abs(h_x - h_y) <= d`. Without that consistency, the intersection formula could fall below a required endpoint. After propagation, there is enough horizontal distance to connect the limits with steps of size at most one, and the mountain envelope realizes the formula.

**Trace the first example.** Add anchor `[1, 0]` to restrictions `[2, 1]` and `[4, 1]`, then append `[5, 4]` as the harmless right boundary. Propagation lowers the last bound to two because it is only one step from building four’s height-one limit. Interval peaks are one between buildings one and two, two between two and four, and two between four and five. The maximum is two.

With no explicit restrictions, the anchors are `[1, 0]` and `[n, n - 1]`. Their formula returns `n - 1`, corresponding to heights zero through `n - 1`.

**Why checking only anchor intervals is complete.** Every building lies either at an anchor or between two consecutive anchors. In an interval without another explicit restriction, only its adjusted endpoint limits can be the active constraints; all farther restrictions have already been propagated into those endpoints. The formula gives the exact highest possible building in that interval. Taking the maximum over every interval therefore covers all `n` buildings without enumerating them.

## Complexity detail

Let `r` be the original number of explicit restrictions. Adding at most two anchors changes the count only by a constant. Sorting takes `O(r log r)` time. The two propagation passes and peak scan are linear, so total time is `O(r log r)`.

The algorithm reuses and mutates the restriction list. Apart from sorting’s implementation-dependent temporary storage, it keeps only scalar variables and at most two appended rows. Python’s sort may use `O(r)` auxiliary memory, so an overall `O(r)` auxiliary bound is safe. It never allocates anything proportional to `n`.

## Alternatives and edge cases

- **Enumerate every building:** Propagating a full length-`n` limit array is impossible when `n` reaches one billion.
- **Binary search a global height:** One could test whether some building can reach a candidate height, but interval peak formulas provide the exact answer more directly.
- **No explicit restrictions:** The default anchors yield the increasing sequence with maximum `n - 1`.
- **Restriction already at building `n`:** It serves as the final anchor, so the harmless `[n, n - 1]` row is not added.
- **Very loose restriction:** Propagation lowers it when a neighboring or fixed-boundary constraint is tighter.
- **Zero-height restriction:** Its cone may force nearby buildings low, and both passes carry that effect in each direction.
- **Odd versus even interval balance:** Integer floor handles a peak lying between two building positions.
- **Endpoint peak:** Propagated consistency ensures the formula includes cases where the highest feasible value occurs at an interval boundary.
- **Fixed first building:** Appending `[1, 0]` makes its rule participate in the same propagation logic.
- **Input mutation:** The exact source appends rows, sorts the list, and rewrites height fields. Callers needing preservation must pass a deep enough copy.
- **Large indices and heights:** Python integer arithmetic safely handles sums near billions; fixed-width implementations should use a wide integer type.
