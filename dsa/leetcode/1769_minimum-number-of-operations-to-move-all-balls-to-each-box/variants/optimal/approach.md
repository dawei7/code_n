## General

**Split each target's cost into left and right contributions**

Moving a ball from position `p` to target `i` costs `abs(p - i)` operations. Balls to the left contribute `i - p`, while balls to the right contribute `p - i`. A ball already at `i` contributes zero.

The exact solution builds:

- `left[i]`, the total distance from all balls strictly left of `i` to `i`.
- `right[i]`, the total distance from all balls strictly right of `i` to `i`.

The final answer at `i` is `left[i] + right[i]`.

**Derive the left-to-right recurrence**

`left[0]` is zero because no box lies to the left of index zero. `cnt` tracks how many balls lie in positions already passed.

Before computing `left[i]`, the code checks `boxes[i - 1]` and increments `cnt` if that box contains a ball. At that moment, `cnt` is exactly the number of balls at indices less than `i`.

Imagine moving the target from `i - 1` one step right to `i`. Every ball on the left becomes one step farther away, so the total cost increases by the number of those balls. Therefore:

`left[i] = left[i - 1] + cnt`.

For example, if three balls lie to the left, shifting the destination right by one requires one additional move from each, adding three.

**Derive the right-to-left recurrence**

The second pass is symmetric. `right[n - 1]` is zero because no box lies to the right of the last index. `cnt` is reset to zero.

When computing `right[i]`, the source first includes a possible ball at `boxes[i + 1]`. `cnt` then equals the number of balls strictly right of `i`.

Moving the target from `i + 1` one step left to `i` increases every right-side ball's distance by one. Thus:

`right[i] = right[i + 1] + cnt`.

The loop moves from `n - 2` down to zero so the needed state `right[i + 1]` is already known.

**Why the ball in the target box is excluded**

The left pass counts positions less than `i` by reading `i - 1` before computing target `i`. The right pass counts positions greater than `i` by reading `i + 1`.

Neither includes `boxes[i]` in the cost for target `i`. That is correct because a ball already in the target needs zero operations. It will enter `cnt` only when calculating a target farther away in a later loop iteration.

**Trace boxes 110**

Initialize both arrays to zero.

In the left pass:

- At target one, box zero contains a ball, so `cnt = 1` and `left[1] = 1`.
- At target two, box one contains a ball, so `cnt = 2` and `left[2] = 1 + 2 = 3`.

Thus `left = [0,1,3]`.

In the right pass, no ball lies right of index one or zero except those already on their left sides, so `right = [1,0,0]`: specifically, the ball at index one contributes one to target zero.

Elementwise addition gives `[1,1,3]`.

**Why each array has its stated meaning**

For the left pass, assume `left[i - 1]` is the sum of distances from balls before `i - 1` to that target. After including a possible ball at `i - 1`, `cnt` counts all balls before `i`. Shifting the target right adds one distance unit for each, proving the recurrence and invariant by induction.

The symmetric argument proves `right[i]` is the total distance from balls after `i`.

Every ball is either left of, at, or right of a target. The at-target contribution is zero, while the other two disjoint sets are exactly represented by `left` and `right`. Their sum is therefore the minimum required number of adjacent moves.

**Why summing distances is optimal**

Each operation moves one ball one box. A ball at `p` must traverse at least `abs(p-i)` edges to reach `i`, and moving it directly along the line achieves exactly that many. Balls do not block each other, and multiple balls may share a box.

Therefore individual minimum distances add independently; there is no scheduling interaction that could reduce or increase the required total.

## Complexity detail

Let $n$ be the number of boxes. The left pass, right pass, and final `zip` comprehension each visit $n$ entries with constant work. Total time is $O(n)$.

`left` and `right` each contain $n$ integers, and the returned comprehension creates a third list of length $n$. Peak storage is $O(n)$, matching the manifest. Scalar counters and indices use $O(1)$ additional space.

The input string is read only. Python integers safely hold the largest total distance under the constraints.

## Alternatives and edge cases

- **One combined bidirectional loop:** Accumulate left and right costs into one answer list in a single outer loop, reducing the number of full arrays while retaining $O(n)$ time.
- **Brute-force every target and ball:** Direct distance summation takes $O(n^2)$ time.
- **Prefix counts and position sums:** Mathematical prefix formulas also answer each target in $O(1)$ after linear preprocessing, but use similar storage.
- **No balls:** Both arrays remain zero and every answer is zero.
- **One ball:** Results are its distances to all target indices.
- **Ball at current target:** It contributes zero and is excluded from both strict-side counts.
- **Multiple balls after moves:** The calculation concerns the initial state independently for every target, so simulated states are irrelevant.
- **Single box:** Both passes are empty and the result is zero whether or not it contains a ball.
- **All boxes contain balls:** Counts grow on each pass, producing symmetric distance totals.
- **Reset cnt:** The right pass must start with zero; retaining the left count would corrupt all values.
- **Loop bounds:** The left pass begins at one and the right pass at `n - 2` because boundary costs are already zero.
- **Binary characters:** Comparing with `'1'` directly determines whether to increment the count.
- **Elementwise sum:** `zip(left, right)` aligns contributions for the same target index.
- **Input preservation:** No actual balls are moved and `boxes` is unchanged.
