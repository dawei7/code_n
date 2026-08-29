## General

**Track only the difference between the two supports**

Each rod has three choices: ignore it, weld it to the currently taller support, or weld it to the currently shorter support.

Remembering both support heights creates redundant states. Future feasibility depends on their absolute difference. The recursion uses `dfs(i, j)`, where `i` is the next rod index and `j` is the current nonnegative height difference.

The returned value is the maximum additional contribution to the shorter support obtainable from rods `i` onward while eventually returning the difference to zero.

**Base case**

When `i >= len(rods)`, no rods remain. If `j == 0`, the two sides are equal, so the return is zero. If `j != 0`, the branch can never form a valid billboard and returns negative infinity.

The impossible sentinel prevents an unequal branch from winning a maximum merely because it accumulated earlier height.

**Choice one: skip the rod**

Ignoring `rods[i]` changes neither the difference nor the shorter height. Its result is `dfs(i + 1, j)`. Unused rods are allowed, so this choice must always exist.

**Choice two: add the rod to the taller support**

Placing length `r` on the taller side increases the difference from `j` to `j + r`. It does not raise the shorter side, so the candidate is `dfs(i + 1, j + r)`.

The code combines skip and taller-side placement in its first `max`.

**Choice three: add the rod to the shorter support**

Adding length `r` against difference `j` produces new difference `abs(r - j)`.

The common supported height rises by:

- `r` when `r <= j`, because the shorter side remains shorter;
- `j` when `r > j`, because it closes the gap and then becomes taller.

Both cases equal `min(j, r)`. The candidate is:

`dfs(i + 1, abs(r - j)) + min(j, r)`.

This formula avoids tracking which physical side is left or right. If the shorter side overtakes the taller one, their labels simply swap.

**Trace of the shorter-side formula**

Suppose support heights are eight and five, so `j = 3`.

Adding a rod of two to the shorter side produces eight and seven. Common height rises by two, and the new difference is one.

Adding a rod of five produces eight and ten. The previous three-unit gap closes, so common baseline rises by three. Roles swap, and the new difference is two. These are exactly `min(3, 5) = 3` and `abs(5 - 3) = 2`.

**Why `dfs(0, 0)` is the answer**

Initially both supports have height zero and difference zero. Every shorter-side placement adds exactly the increase in their common baseline. Taller-side placements contribute only when later rods close their difference.

A branch is accepted only if it finishes at difference zero. Its accumulated contribution is then the equal height of both supports.

The recursion takes the maximum across all three choices for every rod, so the initial state returns the tallest achievable equal supports.

**Why memoization matters**

Different earlier assignments can reach the same pair `(i, j)`. From that point, remaining choices are identical. `@cache` computes each state once instead of expanding an exponential three-way tree repeatedly.


Every legal decision for current rod is exactly skip, taller, or shorter. The three transitions update difference and shorter-height gain exactly.

Assume recursive results are optimal for states beginning at `i + 1`. Taking the maximum of all current legal choices gives the optimal completion at `(i, j)`. Terminal states accept exactly equality. Backward induction proves the initial result.

**Why the difference state is bounded**

Each support height is a sum of processed rods, so their absolute difference can never exceed `S`, the sum of every rod. This finite limit is what gives at most `S + 1` possible difference values for each rod index.

## Complexity detail

Let `N` be rod count and `S` total rod length. Difference `j` ranges from zero through `S`, yielding at most `O(NS)` memoized states. Each performs constant work, so time is `O(NS)`.

The exact cache may retain `O(NS)` results, and recursion uses `O(N)` stack depth. Its space is `O(NS)`, not the manifest's `O(S)`. The smaller bound requires an iterative rolling difference table.

## Alternatives and edge cases

- **Iterative difference DP:** Map each difference to the best shorter height and update per rod. It gives `O(NS)` time and `O(S)` space.
- **Meet in the middle:** Enumerate three choices per rod in each half and combine matching differences, useful because `N` is only twenty.
- **Unmemoized recursion:** It explores `O(3^N)` assignments.
- **No positive solution:** Skipping every rod ends at difference zero and returns zero.
- **One rod:** It cannot make two positive equal supports, so the answer is zero.
- **Rod exactly closes the gap:** New difference is zero and the full gap is added.
- **Rod exceeds the gap:** Support roles swap; absolute difference handles this automatically.
- **Negative infinity:** A finite addition to an impossible suffix remains impossible.
- **Unused rods:** The skip branch is essential because not every rod must be used.
- **Symmetric supports:** Absolute difference avoids duplicate left-right states.
