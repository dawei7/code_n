## General

**Maintain the best and worst product ending here**

The competitive solution uses:

- `local_max`: largest product of a nonempty subarray ending at the current position;
- `local_min`: smallest product of a nonempty subarray ending there;
- `global_max`: largest product found at any ending.

The minimum is just as important as the maximum. A negative current value can turn the smallest negative product into the largest positive one.

Before reading the first element, both local states are initialized to one and the global result to negative infinity. The first update considers `x`, `1 * x`, and `1 * x`, so both local states become the first value. This effectively establishes the normal nonempty base case inside the loop.

**Enumerate the only three endpoint choices**

For each new `x`, a subarray ending there either:

- consists only of `x`;
- extends the previous local maximum;
- extends the previous local minimum.

The new maximum is the maximum of those three products, and the new minimum is their minimum.

No other previous ending product needs to be stored. Multiplication by a positive value preserves order, so extrema remain extremal. Multiplication by a negative value reverses order, swapping their roles. Multiplication by zero maps every extension to zero.

**Why tuple assignment is essential**

The source updates both local values in one assignment:

`local_max, local_min = new_max_expression, new_min_expression`

Python evaluates both right-hand expressions before assigning either variable. Thus both calculations use the old `local_max` and old `local_min`.

If `local_max` were assigned first in a separate statement, the `local_min` expression could mix products from two different iteration states and cease to represent subarrays ending at one coherent index.

**Update the global result after the local state**

`local_max` answers only for subarrays ending at the current element. The desired subarray may end anywhere, so `global_max` retains the best local maximum observed.

Every nonempty subarray has an ending index, and the recurrence evaluates the exact maximum for each ending. The maximum across those states is therefore the complete answer.

**Zeros and negative values require no special branches**

At zero, all three candidates are zero, resetting both local states. The global answer keeps any positive product found before zero, while later subarrays begin independently.

At a negative value, the `local_min * x` candidate can rescue a previously negative chain. At the first negative in a chain, the one-element `x` candidate ensures a valid nonempty state remains even if every extension is worse.

For `[2,3,-2,4]`, `global_max` reaches six after the second value. The negative changes the local extremes dramatically, but the later four does not exceed the saved six.

For an all-negative single-element input, negative infinity is replaced by that element’s local maximum during the first loop, so the function never incorrectly chooses an empty product of one.

**The primary and secondary classes**

The selected class is the first class named `Solution`. `Solution2` is a related sign-branch formulation but is not the selected implementation.

The primary loop reads the original input directly and creates no slice or copy.

The recurrence stores products rather than the subarray boundaries because the contract asks only for the product. If the actual subarray were required, start indices would need to accompany both local extrema and the global choice; the value-only state is sufficient here.

## Complexity detail

Let $n$ be the array length.

The loop performs a constant number of multiplications and comparisons per element, giving $O(n)$ time.

Only three persistent numeric states and the loop variable are stored. Auxiliary space is $O(1)$, matching the manifest.

`float("-inf")` is used only as an initial value below any legitimate product. After the first valid element, `global_max` becomes an integer. The contract guarantees nonempty input and 32-bit intermediate products.

## Alternatives and edge cases

- **Initialize from the first element:** Set all three states to `nums[0]` and loop from index one. It avoids the negative-infinity sentinel but must avoid a slicing copy to preserve constant space.
- **Swap extrema on a negative:** Exchange maximum and minimum before updating with `x`; this makes the sign reversal explicit.
- **Two directional product scans:** Scan prefixes from left and right, resetting after zeros. It achieves the same asymptotic bounds with different reasoning.
- **Quadratic enumeration:** Multiply every subarray from each start. It is straightforward but too slow for $n=2\cdot10^4$.
- **Single element:** The first update returns it even when it is negative.
- **Zero among negatives:** Zero may be the maximum and prevents combining noncontiguous values across it.
- **All positives:** `local_max` grows through the chain while `local_min` is still maintained harmlessly.
- **Two negatives:** The old minimum multiplied by the second negative can become the maximum.
- **Nonempty input:** An unsupported empty list would return negative infinity, not an integer answer.
- **Simultaneous-state requirement:** Sequentially overwriting one local extreme before computing the other is a common correctness bug.
- **No overflow in Python:** Python integers expand, while fixed-width implementations may rely on the stated intermediate-product guarantee.
