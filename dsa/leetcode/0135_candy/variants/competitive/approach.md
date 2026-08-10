## General

**Use one array, but enforce one direction at a time**

The candy rule is directional even though it is stated for both neighbors. A child with a higher rating than the left neighbor must receive more candy than that neighbor, and a child with a higher rating than the right neighbor must receive more than that neighbor.

The competitive solution begins with `candies[i] = 1` for every child. This is the smallest possible base assignment. It then makes one forward pass to satisfy rising edges from the left and one backward pass to repair falling edges from the right.

The important principle is monotonic repair: the second pass may raise candy counts, but it never lowers a count established by the first pass. Consequently, satisfying the right-side constraints cannot destroy the left-side constraints.

**First pass: minimum counts for left comparisons**

For indices from one through `n - 1`, the code checks whether the current rating exceeds the previous rating.

If it does, the current child needs strictly more candy than the left neighbor. Assigning `candies[i - 1] + 1` is the smallest integer that works.

If it does not, the left neighbor creates no lower bound beyond the universal one, so the initial value one remains.

After this pass, every edge where the rating rises left-to-right has a corresponding candy rise. Increasing rating runs receive counts `1, 2, 3, ...` from their lowest point. The array is minimal if only left-neighbor rules are considered.

**Second pass: repair right comparisons without breaking the first pass**

The loop `reversed(range(1, len(ratings)))` produces `n - 1, n - 2, ..., 1`. It compares child `i - 1` with child `i`, thereby visiting edges from right to left.

When `ratings[i - 1] > ratings[i]`, the left child must have more candy than the right child. A repair is necessary only if `candies[i - 1] <= candies[i]`. In that case, the code sets the left count to `candies[i] + 1`.

This condition is equivalent to assigning:

`candies[i - 1] = max(candies[i - 1], candies[i] + 1)`

on every decreasing rating edge. The explicit comparison avoids an assignment when the existing value is already sufficient.

Why can raising `candies[i - 1]` not break the rule with its own left neighbor? If the first pass required `candies[i - 1]` to exceed that neighbor, making it larger preserves the inequality. If no such requirement existed, raising it does not create a violation because rules constrain the higher-rated child, not arbitrary candy differences.

Moving right-to-left is essential. When processing edge `(i - 1, i)`, `candies[i]` already includes every amount needed to dominate a decreasing chain farther right. The new value can therefore propagate that requirement one position left.

**Why the resulting assignment is minimum**

The forward pass gives each position its smallest left-direction lower bound. The backward pass raises a position only when its right neighbor proves the current value invalid, and then raises it to exactly one more than that neighbor.

Equivalently, the finished value at each position is the maximum of:

- the minimum count demanded by an increasing run from the left;
- the minimum count demanded by a decreasing run toward the right.

Every valid distribution must meet both lower bounds. Using their maximum meets both and adds no unnecessary candy. Summing the finished array therefore yields the globally minimum total.

At a peak, the forward pass may already assign a large value. If a shorter right descent requires less, the `<=` condition leaves that larger value untouched. If the right descent is longer, the backward pass raises the peak enough to dominate that side. This is exactly why overwriting unconditionally with `candies[i] + 1` would be wrong: it could reduce a peak below the count required by its left ascent.

**Trace the two examples**

For `[1, 0, 2]`, initialization gives `[1, 1, 1]`. The forward pass raises the last child to two. The backward pass sees that rating one at index zero exceeds rating zero at index one and raises the first child to two. The final `[2, 1, 2]` sums to five.

For `[1, 2, 2]`, the forward pass produces `[1, 2, 1]`. The equal final ratings create no constraint, and the backward pass makes no change. The sum is four.

## Complexity detail

Let $n$ be the length of `ratings`.

Initialization creates $n$ entries. Each directional pass examines $n-1$ adjacent pairs, and `sum(candies)` reads $n$ integers. The total time is $O(n)$.

The `candies` array uses $O(n)$ auxiliary space. Loop variables and the final integer sum require $O(1)$ additional space. The input ratings are not modified.

The manifest’s $O(n)$ time and $O(n)$ space accurately describe this source. The reversed range is lazy in Python 3 and does not create another length-$n$ list.

## Alternatives and edge cases

- **Two directional arrays:** Store left-only and right-only requirements separately, then sum their elementwise maxima. It is particularly clear but uses two $O(n)$ arrays instead of one.
- **Constant-space slope method:** Count ascending and descending run lengths and use triangular sums, assigning a peak to the longer side. It saves memory but has more delicate transitions around plateaus.
- **Repeated local repairs:** Scan until no inequality is violated. It converges but may propagate a long chain only one step per pass and take $O(n^2)$ time.
- **Sort by rating:** Assign low-rated children first and derive higher-rated counts from processed neighbors. It works but costs $O(n\log n)$.
- **One child:** Initialization gives one and both passes are empty.
- **Equal adjacent ratings:** They impose no strict candy relationship, so neither comparison updates solely because of equality.
- **Strict ascent:** The first pass alone builds `1` through `n`; the backward pass changes nothing.
- **Strict descent:** The first pass leaves ones, and the backward pass builds `n` down to one.
- **Mountain peak:** The conditional backward update preserves a taller left-side requirement or raises it for a taller right-side requirement.
- **Valley:** The lowest-rated child can retain one while both surrounding sides rise away from it.
- **Empty input outside the contract:** This source would return zero. The Reference requires at least one child, so that behavior is not part of the promised interface.
