## General

**View the random process as choosing the first box's balls.** There are `2n` balls total, and the first `n` positions of a uniformly random shuffle go to box one. Conceptually label balls even when they share a color. Every subset of `n` labeled balls is equally likely to occupy those positions, so the total number of equally likely selections is `comb(2n, n)`.

Once box one's selection is fixed, all remaining balls go to box two. The algorithm counts how many size-`n` selections give both boxes the same number of represented colors, then divides by the total.

**Choose a quantity for each color.** For color `i`, let `x` be the number of its `balls[i]` balls sent to box one. Then the other box receives `balls[i] - x`. The loop considers every integer `x` from zero through the complete color count.

Although balls of one color look identical in the output condition, there are `comb(balls[i], x)` ways to choose which labeled balls of that color enter box one. Multiplying these binomial factors across colors gives the number of equally likely labeled selections represented by one vector of per-color quantities.

Ignoring these weights would incorrectly treat all color-count distributions as equally likely. For example, splitting one of two same-color balls between boxes has two labeled choices, while sending both together has only one.

**Define the memoized state.** `dfs(i, j, diff)` counts favorable labeled selections using colors from index `i` onward, given that box one still needs exactly `j` balls. `diff` is the number of distinct colors currently exclusive to box one minus the number currently exclusive to box two.

Colors split between both boxes contribute one distinct color to each, so their net difference is zero. Colors wholly assigned to one box contribute only to that box's distinct count.

The initial call `dfs(0, n, 0)` has processed no colors, must still fill all `n` positions in box one, and has no distinct-color difference.

**Update the distinct-color difference correctly.** If `x == balls[i]`, every ball of the current color goes to box one. Box one contains that color and box two does not, so `y = 1`.

If `x == 0`, the color appears only in box two, so `y = -1`. For any strict split, both boxes contain the color, so `y = 0`.

The recursive call becomes `dfs(i + 1, j - x, diff + y)`. Multiplying by `comb(balls[i], x)` weights that branch by its number of labeled choices.

**Interpret the base cases.** If `j < 0`, too many balls have already been assigned to box one, so the branch is impossible and returns zero.

When `i >= k`, every color has been assigned. A favorable distribution must have filled box one exactly, so `j == 0`, and must have equal distinct-color counts, so `diff == 0`. The function returns one only when both conditions hold.

The returned one represents one completion at the per-color allocation level; binomial factors accumulated on the way back expand it into the correct number of labeled selections.

**Trace the simplest case.** For `balls = [1, 1]`, each box receives one ball. For the first color, choosing its ball for box one adds one to `diff`; leaving it for box two subtracts one. To finish with one ball and difference zero, the second color must go to the opposite box. There are two favorable selections out of `comb(2,1) = 2`, giving probability one.

For a color count of two, assigning one ball to each box has coefficient `comb(2,1) = 2` and changes `diff` by zero. Assigning both to one side has coefficient one and changes the difference by positive or negative one.

**Why memoization is valid.** Once the first `i` colors have been summarized by remaining capacity `j` and distinct-count difference `diff`, their detailed allocation no longer affects future choices. All future weights depend only on unprocessed color counts. Different histories reaching the same state therefore have identical completion counts and can share one cached result.

**Why numerator divided by denominator is the probability.** Each root-to-leaf allocation chooses exactly `n` labeled balls when `j` ends at zero. The product of binomial coefficients counts how many labeled subsets realize that allocation. Different allocation vectors are disjoint, and together they cover every size-`n` subset. The DFS numerator keeps exactly those with zero distinct difference. Dividing by `comb(2n,n)` therefore gives the desired uniform probability.

The boxes are distinguished throughout: choosing a ball for box one versus leaving it for box two is not identified with the reversed allocation.

## Complexity detail

Let `K` be the number of colors, `n` the capacity of one box, and `B` the maximum count of one color. The state variables have up to `K` values for `i`, `n + 1` relevant values for `j`, and `O(K)` possible differences from `-K` through `K`.

There are therefore `O(K^2 n)` potential cached states. Each state tries at most `B + 1` values of `x`, giving `O(K^2 n B)` time, matching the manifest's time bound.

The exact cache can hold `O(K^2 n)` results because `diff` is a genuine state dimension. The recursion stack uses `O(K)`. The manifest's `O(Kn)` space omits the possible distinct-difference dimension and understates this exact implementation's general cache bound.

With the given small limits, the state space is manageable. `comb` operates on small integers, and intermediate counts remain exact Python integers until the final floating-point division.

## Alternatives and edge cases

- **Bottom-up dynamic programming:** Process colors while tracking box-one count and distinct-count difference. It has the same conceptual state and can avoid recursion.
- **Enumerate all x vectors without caching:** It repeats equivalent suffix subproblems and grows roughly as the product of all `balls[i] + 1` choices.
- **Treat color allocations equally:** This is wrong because different `x` values have different binomial multiplicities.
- **Track both distinct counts:** Two separate counters are sufficient but redundant; only their difference is needed for equality.
- **Prune excessive remaining capacity:** A branch can also return zero when remaining balls cannot fill `j`. The stored source relies on the final base test instead.
- **All colors have one ball:** Every selected ball introduces a box-exclusive color, so equality depends on selecting the same number of colors for each box.
- **A color is split:** It contributes one distinct color to both boxes and changes `diff` by zero.
- **A color stays entirely together:** It contributes positive or negative one depending on which box receives it.
- **Boxes are different:** Reversing assignments generally represents a separate equally likely outcome, even though favorable status is symmetric.
- **Even-total guarantee:** `sum(balls) >> 1` is exactly one box's capacity because the total is even.
- **Impossible overfill:** Negative `j` branches return zero immediately.
- **Underfilled box one:** Reaching the end with positive `j` fails the base condition.
- **Equal ball counts but unequal distinct counts:** Capacity alone is insufficient; `diff` must also be zero.
- **Exact arithmetic:** The DFS numerator and binomial denominator are integers; only the final quotient is floating point.
- **Cache-space reporting:** Include the `diff` range, yielding `O(K^2 n)` for this exact source.
