## General

**Turn equal partitioning into one subset-sum target**

Let the total of all array elements be $S$. If the array can be divided into two subsets with equal sum, each subset must sum to $S/2$. This immediately gives two conclusions.

First, an odd total can never work because two integer subset sums cannot both equal a non-integer half. The solution computes

`m, mod = divmod(sum(nums), 2)`.

Here `m` is the integer quotient and `mod` is the remainder after division by two. If `mod` is `1`, the total is odd and the method returns `False` immediately.

Second, when the total is even, it is enough to ask whether some subset sums to `m`. If such a subset exists, all elements not selected for it form the other subset. Their sum is `2 * m - m = m`, so the two parts are equal. Conversely, any equal partition necessarily supplies a subset of sum `m`. The problems are therefore equivalent.

Because every `nums[i]` is positive, only target sums from zero through `m` need to be represented.

**Define the dynamic-programming state precisely**

The solution allocates

`f = [[False] * (m + 1) for _ in range(n + 1)]`.

The Boolean state `f[i][j]` means:

> Using only the first `i` array elements, is it possible to select a subset whose sum is exactly `j`?

Rows represent how many input elements are available, not an array index that must be selected. Columns represent candidate sums. This definition turns the original choice among many subsets into a table of reusable yes-or-no subproblems.

The base state `f[0][0] = True` says that with no elements, selecting the empty subset achieves sum zero. Every other state in row zero remains false: no positive sum can be formed without elements.

Although the final partition uses all input elements between its two sides, the chosen target subset may be empty only when the target is zero. Here all values are positive and the input is non-empty, so a valid even total has positive target; the ordinary transitions handle it without a special case.

**For each element, choose it or leave it for the other subset**

The outer loop uses `enumerate(nums, 1)`, so `i` runs from `1` through `n`, and `x` is the newly available element. For every target `j` from zero through `m`, there are exactly two ways `f[i][j]` can become true.

The first option excludes `x`. If the first `i-1` elements could already make `j`, then those same selections remain available after introducing `x`. This is `f[i - 1][j]`.

The second option includes `x`. This requires `j >= x`; otherwise including a positive `x` would overshoot `j`. If it fits, the remaining selected elements must sum to `j - x` using only the preceding `i-1` elements. This is `f[i - 1][j - x]`.

The exact transition is therefore

`f[i][j] = f[i - 1][j] or (j >= x and f[i - 1][j - x])`.

Python's short-circuit evaluation matters slightly: when `j < x`, the second table access is not evaluated, so no negative column is used.

Both branches read only row `i - 1`. That guarantees each input occurrence is used at most once. Reading from the current row during the include branch could allow the same positive value to be added repeatedly, which would solve an unbounded-knapsack problem instead of the required 0/1 choice.

**A small table trace**

For `nums = [1,5,11,5]`, the total is `22`, so `m = 11`. Initially only sum `0` is reachable.

After processing `1`, sums `0` and `1` are reachable. After processing the first `5`, sums `0`, `1`, `5`, and `6` are reachable: `5` comes from choosing the new element alone, and `6` comes from adding it to the prior reachable sum `1`.

When `11` is processed, `f[3][11]` becomes true because `f[2][0]` is true and including `11` fills the entire target. Later rows preserve this truth through the exclude branch. The returned `f[4][11]` is true, corresponding to subset `[11]`; its complement `[1,5,5]` also sums to `11`.

For `[1,2,3,5]`, the total is `11`, `mod` is nonzero, and no table is needed. Equal integer subset sums are impossible.

**Why the recurrence is complete**

Consider any subset of the first `i` elements that sums to `j`. It either omits element `x` or includes it; there is no third possibility. If it omits `x`, it is represented by `f[i-1][j]`. If it includes `x`, removing that occurrence leaves a subset of the first `i-1` elements with sum `j-x`, represented by the second branch.

Conversely, either true branch constructs a valid subset: preserve a previously known subset, or append the current element to one totaling `j-x`. By induction over rows, every true table cell corresponds to a real subset and every real reachable sum is marked true.

Thus `f[n][m]` is true exactly when some subset of the complete array reaches half the total. The earlier equivalence then proves that this return value exactly answers whether an equal partition exists.

## Complexity detail

Let $n$ be `len(nums)` and let $T = S/2$ be the target `m` when the total is even. The table has $(n+1)(T+1)$ cells, and each cell is filled with constant work. The time complexity is $O(nT)$. Computing the total adds $O(n)$ time and does not change the bound.

The exact shipped implementation allocates the full two-dimensional table, so its auxiliary-space complexity is $O(nT)$. The variant manifest lists $O(T)$ space, but that bound would require the one-dimensional compression described below; it is not the space used by this exact `f` table. Accurately following the code therefore requires reporting $O(nT)$ space here.

With the constraints, $S \le 200 \cdot 100 = 20000$, so $T \le 10000$. This is pseudo-polynomial dynamic programming: its cost is polynomial in the numeric target value, not merely in the number of bits needed to encode that value.

## Alternatives and edge cases

- **One-dimensional 0/1 subset-sum DP:** Keep only `f[j]` and update `j` from `T` down to `x`. Descending order ensures each occurrence is used once and reduces space to $O(T)$ while retaining $O(nT)$ time. This is the implementation needed to meet the manifest's stated space bound.
- **Update a one-dimensional table upward:** Iterating from `x` to `T` is incorrect here because newly set states can reuse the same element again in the same iteration, turning the problem into unbounded subset sum.
- **Top-down recursion with memoization:** Cache states `(i, remaining)`. It has the same $O(nT)$ worst-case state count and can stop early, but adds recursion overhead and stack depth.
- **Enumerate all subsets:** Include/exclude recursion without memoization takes $O(2^n)$ time and repeats equivalent remaining-sum states.
- **Bitset of reachable sums:** Repeatedly compute a shifted bitset and OR it into the current one. This compact technique is fast, but the Boolean-table transition is often easier for beginners to derive.
- **Odd total:** The immediate `False` return is logically decisive and avoids allocating a table for an impossible target.
- **One element:** Its positive total either is odd or has a half smaller than the element; no subset can form an equal nonempty complement, so the method returns false.
- **Duplicate numbers:** Each occurrence owns a separate DP row and may be selected independently. Equal values are not collapsed.
- **All values positive:** Positivity justifies limiting columns to `0..T` and makes overshooting irreversible. The contract excludes negative or zero complications.
- **An element larger than the target:** Its include branch is unavailable for every column, so its row simply copies the preceding row.
- **A direct element equal to the target:** The state `f[i][T]` becomes true from `f[i-1][0]`, and the complement automatically has the same sum.
