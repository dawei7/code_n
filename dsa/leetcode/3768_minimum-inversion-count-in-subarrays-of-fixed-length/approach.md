## General

**Reuse the inversion count when the window moves**

There are $N-K+1$ length-`k` windows. Counting every pair independently inside every window would require $O(K^2)$ work per window.

Two consecutive windows share `k-1` elements in the same relative order. Sliding right removes only the old leftmost element and adds only one new rightmost element. Every inversion between two retained elements is unchanged. Therefore the current inversion count can be updated by:

1. subtracting inversions involving the outgoing leftmost value;
2. adding inversions involving the incoming rightmost value.

The challenge is to count smaller or larger current values quickly. A Fenwick tree stores value frequencies and answers prefix-count queries in logarithmic time.

**Compress values without changing comparisons**

`nums[i]` may be as large as $10^9$, so using the value directly as a Fenwick index would waste enormous space. The source creates

`values = sorted(set(nums))`

and maps a value to

`bisect_left(values, value) + 1`.

This is a one-based rank, as required by the Fenwick implementation. Coordinate compression preserves order:

$$
a<b \iff \operatorname{rank}(a)<\operatorname{rank}(b).
$$

Equal values receive the same rank. That is essential because equality is not an inversion.

**Interpret the Fenwick tree as a frequency table**

`add(rank, 1)` inserts one occurrence, while `add(rank, -1)` removes one. Repeated values are represented by a frequency greater than one rather than by separate ranks.

`prefix_sum(r)` returns the number of stored elements whose rank is at most `r`. Consequently:

- `prefix_sum(r - 1)` counts values strictly smaller than rank `r`;
- `prefix_sum(r)` counts values less than or equal to rank `r`;
- `window_size - prefix_sum(r)` counts values strictly greater than rank `r`.

The strict/non-strict boundary changes between these formulas deliberately so duplicates never become inversions.

Internally, `index & -index` isolates the lowest set bit. Addition moves upward through Fenwick ranges with `index += index & -index`; a prefix query moves toward zero with `index -= index & -index`. Each move changes at least one binary position, so only $O(\log U)$ cells are visited, where $U$ is the number of distinct values.

**Count the first window from left to right**

Before inserting `nums[index]`, the tree contains exactly the earlier elements of the first window. The current value will be the right endpoint of every new pair.

If its compressed rank is `r`, then `prefix_sum(r)` counts earlier values less than or equal to it. There are `index` earlier values in total, so

`index - prefix_sum(r)`

counts earlier values strictly greater than the current value. Those and only those form inversions ending at this position.

After adding this amount to `inversions`, the current rank is inserted for the next iteration. Once the first `k` values have been processed, `inversions` is the exact count for window `nums[0:k]`, and `answer` is initialized to it.

**Remove precisely the outgoing pairs**

When the right boundary moves to `right`, the outgoing value is `nums[right-k]`. It is the leftmost value in the old window. Therefore every inversion involving it has the outgoing value as the left endpoint and a strictly smaller value somewhere to its right.

Before removal, the Fenwick tree still represents the complete old window. For outgoing rank `r`,

`prefix_sum(r - 1)`

counts all stored values strictly smaller than the outgoing value. The outgoing occurrence itself is not included, and equal values are excluded. Because the outgoing element is leftmost, every such smaller stored value lies after it and forms exactly one inversion with it.

The source subtracts this count and then calls `add(r, -1)`. Performing the query before removal is safe because the query excludes the outgoing rank anyway, and it ensures the tree still has the clearly defined old-window state.

**Add precisely the incoming pairs**

After removal, the tree contains the `k-1` retained elements. The incoming value `nums[right]` becomes the rightmost element of the new window, so every new inversion involving it must have a retained value greater than it on the left.

For incoming rank `r`, `prefix_sum(r)` counts retained values less than or equal to it. Thus

`(k - 1) - prefix_sum(r)`

is the number of retained values strictly greater than it. The source adds this number to `inversions` and then inserts the incoming rank.

No pair between retained elements changed order, so the subtraction and addition account for every changed pair and no unchanged pair. The resulting count is exact for the new window.

**Keep the minimum over all window states**

After each slide, `answer = min(answer, inversions)` records the best count seen so far. The loop visits right endpoints `k` through `N-1`, which generates every window after the first exactly once.

The first-window construction establishes the inversion-count state. Each slide preserves it by removing exactly the outgoing contributions and adding exactly the incoming contributions. Therefore every value compared with `answer` is the correct count for its window, and the final minimum covers all candidates.

## Complexity detail

Let $N$ be the array length and $U$ the number of distinct values, with $U\le N$.

Building the set and sorting its values costs $O(N\log N)$ worst-case time. Each of the $N$ array occurrences is ranked by binary search and inserted or removed through $O(\log U)$ Fenwick operations. The total update/query work is $O(N\log U)$, so the complete bound is $O(N\log N)$.

`values` stores $U$ values and `tree` has $U+1$ counters. No window copy is created. Auxiliary space is $O(U)$, which is $O(N)$ in the worst case.

An inversion count can reach $K(K-1)/2$. Python integers handle that range automatically; fixed-width implementations should use a sufficiently wide integer.

## Alternatives and edge cases

- **Recount every window directly:** Enumerating all pairs costs $O((N-K+1)K^2)$ and discards almost all information when the window shifts.
- **Merge-sort inversion counting per window:** This improves one window to $O(K\log K)$ but still repeats work across overlapping windows.
- **Balanced ordered multiset:** It can count values below or above a key while sliding, but a Fenwick tree is simpler after coordinate compression.
- **Count `prefix_sum(r)` when removing:** That would include equal values and the outgoing occurrence's rank, subtracting pairs that are not strict inversions. Removal uses `r-1`.
- **Count `(k-1)-prefix_sum(r-1)` when inserting:** That would treat equal retained values as greater. Insertion subtracts the less-than-or-equal count `prefix_sum(r)`.
- **Remove from the tree before measuring outgoing pairs:** It can be made correct, but the exact source queries first; using `r-1` ensures the outgoing occurrence is not counted.
- **`k=1`:** Initial counts and every slide remain zero because a one-element window has no pair.
- **`k=N`:** Only the first window exists, so the sliding loop is skipped.
- **All values equal:** Every strict-smaller and strict-greater count is zero, producing answer zero.
- **Strictly increasing window:** It has zero inversions and immediately gives the smallest possible answer.
- **Strictly decreasing full window:** It reaches the maximum $K(K-1)/2$ inversions.
- **Duplicate values entering or leaving:** Frequency updates preserve multiplicity while shared ranks enforce strict comparison.
- **Large numeric values:** Compression makes memory depend on distinct count, not the maximum value.
- **Input preservation:** The method does not sort or mutate `nums` itself.
