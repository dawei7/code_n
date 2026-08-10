## General

**Choose a minimum value, then make its subarray as wide as possible.** Suppose `nums[i] = x` is treated as the minimum of a candidate subarray. That subarray can extend left and right while every included value is at least `x`. Because all input values are positive, adding another allowed element increases the sum and leaves the minimum at `x`. Therefore the best subarray represented by index `i` is its widest valid interval.

The solution finds that interval for every index with monotonic stacks, calculates its sum with prefix sums, and takes the maximum product before applying the modulus.

**Find the nearest strictly smaller value on the left.** `left` starts filled with minus one, representing an absent boundary before index zero. Scanning left to right, the stack stores indices with strictly increasing values after the loop’s removals.

For current value `x`, the code pops while `nums[stk[-1]] >= x`. Any larger or equal value cannot be the nearest strictly smaller boundary. After popping, the top, if present, is the closest earlier index whose value is less than `x`, and it is stored in `left[i]`.

Thus every index from `left[i] + 1` through `i` has value at least `x`.

**Find the nearest smaller-or-equal value on the right.** `right` starts filled with `n`, representing an absent boundary after the array. Scanning from right to left, the code pops while `nums[stk[-1]] > nums[i]`. Notice that this comparison is strict, unlike the left pass.

After popping, the right stack top, if present, is the closest later index whose value is less than or equal to the current value. That index is excluded from the current representative’s interval, so its valid rightmost included index is `right[i] - 1`.

**Why the two comparisons differ.** Equal minima need consistent ownership. The left pass crosses equal values because it pops `>=`, while the right pass stops at an equal value because it pops only `>`. This assigns overlapping equal-minimum ranges asymmetrically.

For `[3, 3]`, the first three stops before the second equal value on its right, but the second three crosses the first equal value on its left and can represent the whole array. At least one equal occurrence receives the full useful plateau, while the boundaries remain well defined. Using strict comparisons on both sides could prevent any equal representative from spanning the complete plateau; popping equality on both sides would duplicate ownership, which may still find the value but complicates the invariant.

**Compute interval sums in constant time.** `s = list(accumulate(nums, initial=0))` builds prefix sums where `s[t]` is the sum of indices zero through `t - 1`. The interval represented by `i` is

`[left[i] + 1, right[i] - 1]`.

Its sum is

`s[right[i]] - s[left[i] + 1]`.

Multiplying this by `x = nums[i]` gives that interval’s min-product.

**Why every optimal subarray is considered.** Take an optimal subarray and choose an occurrence of its minimum according to the equal-value ownership convention. The stack boundaries for that occurrence extend at least across the entire subarray and stop only at a value that would be smaller or at the assigned equal boundary. Since all values are positive, expanding to the representative’s full interval cannot reduce its sum and does not lower its minimum below `x`. Its computed product is therefore at least the optimal subarray’s product. Since every computed interval is itself valid, the maximum computed value equals the true optimum.

**Trace the key interval in `[1, 2, 3, 2]`.** For the final value two, the nearest strictly smaller left boundary is index zero containing one, and there is no right smaller-or-equal boundary. Its interval is indices one through three, with sum seven. The product is two times seven, or 14.

**Apply modulo only after maximization.** The generator calculates every full integer product, and `max` chooses the largest. Only then does `% mod` run. Applying modulo to individual products first would change their ordering and could select the wrong subarray. Python integer arithmetic safely represents the intermediate values.

## Complexity detail

Each index is pushed onto and popped from each monotonic stack at most once. The two boundary passes therefore take `O(n)` total time, not quadratic time despite their inner while loops. Prefix-sum construction and the final product scan are also `O(n)`. Overall time is `O(n)`.

`left`, `right`, the stack, and prefix sums each use `O(n)` storage. The product generator is lazy and does not allocate another array. Total auxiliary space is `O(n)`.

## Alternatives and edge cases

- **Expand from every index:** Walking left and right separately for each possible minimum can take `O(n^2)` time.
- **Divide and conquer:** Splitting around minimum values can solve related problems, but efficient minimum selection and sum handling are more complex than the stack method.
- **All values equal:** The asymmetric equality rule lets one occurrence represent the full array, which has the greatest positive sum.
- **Single element:** Both boundaries are sentinels, and its product is the value squared.
- **Strictly increasing array:** Left boundaries are immediate predecessors, while right boundaries are mostly `n`.
- **Strictly decreasing array:** Left boundaries are mostly minus one, while right boundaries are immediate successors.
- **Positive-values dependency:** Widest valid range maximizes the sum because every extension adds a positive amount; this argument would fail with negative values.
- **Equal-boundary comparisons:** `>=` on the left and `>` on the right are deliberate, not interchangeable formatting.
- **Modulo timing:** Maximize raw products first and reduce only the final result.
- **64-bit statement guarantee:** Other languages still need a 64-bit type for products; Python integers avoid overflow.
- **Prefix indexing:** `right[i]` is exclusive, and `left[i] + 1` is inclusive, matching the subtraction formula.
- **Non-empty requirement:** Every index represents at least its own one-element interval.
