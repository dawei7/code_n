## General

**The actual values matter only through three categories.**  A good array must contain, in order:

1. every value smaller than `a`;
2. every value in the inclusive range `[a, b]`;
3. every value larger than `b`.

Call these categories low, middle, and high. The order of two values inside the same category is irrelevant. For example, two middle values may appear in either order because both belong to the same contiguous middle part.

It is helpful to replace each value conceptually with a rank:

- low has rank `0`;
- middle has rank `1`;
- high has rank `2`.

After this replacement, the requirement is simply to make the category ranks non-decreasing. Empty parts need no special handling: an array containing no low values, for example, can still be non-decreasing and therefore good.

**Adjacent swaps turn the problem into counting inversions.**  An inversion is a pair of positions `i < j` whose categories are in the wrong order: the category at `i` should come after the category at `j`. The only possible wrong pairs are:

- a middle value before a later low value;
- a high value before a later low value;
- a high value before a later middle value.

Pairs from the same category are not inversions, and the remaining cross-category pairs already have the required order.

Why does the number of such pairs equal the minimum number of adjacent swaps? Consider one wrong pair. Its two elements begin in reversed relative order, but every good final array must place the lower category first. Their relative order can change only when those two elements cross in an adjacent swap, so every inversion forces at least one swap.

That lower bound is attainable. Repeatedly swap any adjacent categories that are out of order, just as bubble sort would. Each such swap removes exactly one inversion and creates none. When no inversion remains, the categories are non-decreasing and the array is good. Therefore, the minimum number of adjacent swaps is exactly the initial inversion count.

**Count inversions while scanning once from left to right.**  The source does not store the category sequence or perform the swaps. Instead, it keeps only:

- `middle`: the number of middle-category values already seen;
- `high`: the number of high-category values already seen;
- `swaps`: the inversion count accumulated so far.

When the current `value` is low, it must eventually move before every earlier middle and every earlier high. Each of those earlier elements forms one inversion with this low value, so the source adds

`middle + high`

to `swaps`.

When the current value is middle, earlier low values are already in the correct relative order, and earlier middle values are in the same category. Only earlier high values are wrong, so the source adds `high` and then increments `middle`.

When the current value is high, no earlier category forms an inversion with it. A high value is supposed to be after everything else. The source merely increments `high` so that a later low or middle value can count it.

This counts every inversion exactly once, at the moment the inversion's right-hand element is encountered. Nothing is counted twice: a low value adds only pairs ending at that low, and a middle value adds only high-middle pairs ending at that middle.

**Walk through the second example.**  For `nums = [9, 7, 5, 3]`, `a = 4`, and `b = 8`, the categories are

`[high, middle, middle, low]`.

- Reading `9` records one high and adds nothing.
- Reading `7` sees one earlier high, so it adds `1` and records one middle.
- Reading `5` also sees that earlier high, so it adds another `1` and records a second middle.
- Reading `3` is low. It must cross both earlier middle values and the earlier high value, so it adds `2 + 1 = 3`.

The total is `1 + 1 + 3 = 5`, matching the minimum five adjacent swaps.

For the first example, the categories are `[low, middle, low, middle, high, high]`. The second low value has one earlier middle value, producing the only inversion. Thus the answer is `1` without simulating the swap.

**The boundary tests match the inclusive contract.**  The source checks `value < a` first. If that is false but `value <= b` is true, the value belongs to the middle. Consequently, a value equal to `a` or `b` is correctly classified as middle. Only a value strictly greater than `b` reaches the high branch.

The result is reduced modulo `1_000_000_007` at the end because the problem asks for the remainder, not because modular arithmetic affects which arrangement is optimal. Python can accumulate the exact inversion count safely and then take the remainder. Taking the remainder after each addition would also produce the same final remainder, but the exact source keeps the reasoning especially direct.

## Complexity detail

Let `n` be the length of `nums`. The loop visits each element exactly once. Every iteration performs only comparisons, counter updates, and integer additions.

- Time complexity is `O(n)`.
- Auxiliary space complexity is `O(1)`.

The algorithm does not modify `nums` and does not build a categorized copy. The three integer accumulators remain constant in number regardless of `n`.

The unreduced inversion count can be as large as

$$
\frac{n(n-1)}{2},
$$

which is about five billion when `n = 10^5`. That exceeds a signed 32-bit integer. Python integers grow as needed. A fixed-width implementation should accumulate in a 64-bit integer even though the returned value is taken modulo `10^9 + 7`.

## Alternatives and edge cases

- **Actually performing adjacent swaps:** Bubble sorting the three categories reaches a good array, but explicitly moving elements can take `O(n^2)` time. Counting the swaps through inversions obtains the same minimum in one pass.
- **Merge-sort inversion counting:** A general inversion counter works in `O(n \log n)` time and `O(n)` extra space. It is unnecessary here because there are only three ordered categories, so two counters capture every possible inversion.
- **Fenwick tree over category ranks:** A frequency tree could count earlier larger ranks, but a structure for three ranks is needless overhead. `middle` and `high` are the only frequencies each branch needs.
- **Already-good input:** No low ever appears after a middle or high, and no middle appears after a high. Every addition is zero, so the algorithm returns `0`.
- **All values in one category:** Equal-category pairs never need to cross. The relevant counters may grow, but `swaps` remains zero.
- **An empty low, middle, or high part:** The statement explicitly permits empty parts. A missing category simply contributes a count of zero; no separate branch is required.
- **Values equal to `a` or `b`:** Both endpoints belong to the inclusive middle range. The ordered `if value < a` and `elif value <= b` checks implement that boundary exactly.
- **Duplicate values:** Duplicates do not cause extra swaps. Only category order matters, and equal values necessarily have the same category.
- **Stability inside a part:** The algorithm computes the minimum needed to group categories. It does not require or pay for sorting values within any part.
- **Modulo arithmetic:** The minimum is determined using the full inversion count. Returning `swaps % MOD` satisfies the output contract; the modulo must not be used as a comparison criterion for alternative arrangements.
- **Large inversion totals:** A reverse category arrangement can have billions of inversions at the maximum input size. Use 64-bit accumulation outside Python.
- **Input preservation:** The source only reads `nums`. This is useful when callers expect the original ordering to remain available after the method returns.
