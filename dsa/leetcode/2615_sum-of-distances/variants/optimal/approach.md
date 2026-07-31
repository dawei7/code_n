## General

For a fixed index $i$, split matching indices into those to its left and those to its right. If a matching left index is $j<i$, its contribution is $i-j$. Suppose $c$ matching values have already appeared and their index sum is $s$. Their combined contribution is

$$
ci-s.
$$

Scan from left to right while storing, for each value, its occurrence count and the sum of its seen indices. Add the expression above to the answer before inserting the current index, so the current occurrence is never counted against itself.

The right-side contribution is symmetric. Clear the aggregates and scan from right to left. When $c$ matching indices to the right have sum $s$, their contribution is

$$
s-ci.
$$

Add that quantity and then insert the current index into the right-side aggregates.

Each matching index is on exactly one side of $i$. The forward pass sums $i-j$ for every matching $j<i$, and the backward pass sums $j-i$ for every matching $j>i$. Adding the two pass results therefore equals the required sum of absolute index differences for every position.

## Complexity detail

Let $n$ be the array length. Each pass performs expected $O(1)$ hash-table operations per index, so total expected time is $O(n)$. The answer and the count and index-sum maps store at most $O(n)$ entries, giving $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Grouped index lists plus prefix sums:** Collect every index for each value and process each sorted group with prefix sums; this is also $O(n)$ time and space but stores all indices explicitly.
- **Compare every pair:** Adding the distance whenever two values match is straightforward, but costs $O(n^2)$ time.
- **All values unique:** Both aggregate counts remain zero when each index is processed, so the answer is all zeros.
- **All values equal:** Every index interacts with every other index; the aggregate formulas still process the array in linear time.
- **Single element:** There is no distinct matching index, so its result is zero.
- **Large values:** Hash keys support values up to $10^9$ without allocating an array indexed by value.
- **Numeric width:** Distance sums can exceed 32-bit signed range, so fixed-width implementations should use 64-bit totals.
