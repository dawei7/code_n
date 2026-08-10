## General

**First narrow the only range that can contain the answer**

Let $n$ be the array length. The smallest missing positive must lie between $1$ and $n + 1$. To see why, imagine that every number from $1$ through $n$ is present. Those $n$ distinct positive values already occupy all $n$ array positions, so the next missing positive is $n + 1$. Otherwise, at least one value in $[1,n]$ is absent, and the smallest absent value lies inside that range.

This observation makes negative numbers, zero, and values greater than $n$ irrelevant to the answer. They can remain in the array as unusable occupants. The algorithm only needs a constant-space way to record which values from $1$ through $n$ occur.

**Use each array index as a value's home**

Instead of allocating a set, the solution rearranges the input. Value `1` belongs at index 0, value `2` at index 1, and in general value `v` belongs at index `v - 1`. After all possible placements, inspecting index `i` answers whether value `i + 1` was present: if it was present, one copy can occupy its home.

This is a cycle-placement or cyclic-sort idea, but the goal is not to sort arbitrary integers. Only in-range positive values have meaningful homes. An array such as `[100, -4, 1]` does not need to become globally ordered; the useful value `1` only needs to move to index 0.

**Why each index uses a `while`, not a single `if`**

At index `i`, the code examines `nums[i]`. If it is an in-range value `v` and its home does not already contain `v`, the value is swapped into index `v - 1`. That swap brings some other value back into index `i`. The incoming value may also have a valid but different home, so the same index must be reconsidered. A `while` follows this chain until the current occupant is out of range, is already in its home, or is a duplicate whose home already contains the same value.

For `[3, 4, -1, 1]`, index 0 initially contains `3`, so it swaps with index 2 and leaves `3` at its home. Index 0 now contains `-1`, which is ignored. At index 1, `4` moves to index 3; the incoming `1` then moves to index 0. The resulting useful arrangement begins `[1, -1, 3, 4]`. The first index whose expected value is absent is index 1, so the answer is 2.

**The duplicate guard prevents endless swapping**

The full loop condition requires `nums[i] != nums[nums[i] - 1]`. Suppose there are two copies of `2` and one has already reached index 1. When the other copy is encountered, swapping it with index 1 would exchange equal values and change nothing. Repeating the loop would then run forever. The inequality recognizes that value `2` is already represented at its home and leaves the extra copy wherever it is.

The bounds test `1 <= nums[i] <= n` must occur before using `nums[i] - 1` as a semantic home. Python's chained comparisons and `and` short-circuiting ensure the destination access is evaluated only for a valid in-range value. Negative values would otherwise use Python's negative indexing, and a value above $n$ would cause an out-of-range access.

**Why the swap makes measurable progress**

Let `v = nums[i]` when a swap occurs. The guard proves that `v` is in range and its destination does not already contain `v`. After the swap, index `v - 1` contains exactly `v`, so at least one previously incorrect home becomes correct.

The displaced value was not correctly placed at that destination: if index `v - 1` had contained its own correct value, that value would have been `v`, which the guard ruled out. Thus the swap does not destroy a correct home. This gives a global progress measure—the number of correctly homed in-range values increases with every swap—and proves both termination and a linear total number of swaps.

**Reading the rearranged array**

After the placement pass, the second loop scans from index 0 upward. If `nums[i] != i + 1`, then value `i + 1` is absent. It cannot merely be sitting elsewhere: any encountered copy of that value would have been moved to index `i` unless another copy was already there, which would also make the index correct. Since indices are checked in increasing order, the first mismatch is the smallest missing positive.

If every index contains its expected value, all positives from $1$ through $n$ occur. The initial range argument then proves that $n + 1$ is the answer.

**Why the method is correct despite ignored values**

Out-of-range values have no possible influence on whether a number in $[1,n]$ is present. They function only as placeholders that useful values may swap through. Duplicates also need no dedicated storage: one copy at the home index is sufficient evidence of presence, and extra copies cannot create a missing value.

For every $v$ in $[1,n]$, if `v` appears in the input, the placement process eventually either moves a copy to index `v - 1` or finds that a copy is already there. Conversely, if index `v - 1` contains `v`, then `v` certainly appeared in the input because swaps only move existing elements. Therefore, the final index test is an exact presence test, completing the correctness argument.

## Complexity detail

The two explicit `for` loops each visit $n$ indices. Although a `while` is nested inside the first loop, it does not create quadratic work. Every successful swap permanently places an in-range value into its correct home without dislodging another correctly homed value. There are only $n$ homes, so at most $n$ such progress-making swaps occur across the entire pass. The total time is therefore $O(n)$.

The rearrangement uses `n`, loop indices, and one temporary destination index `j`. Swaps occur inside the input list, so no set, Boolean array, or second list proportional to $n$ is allocated. Auxiliary space is $O(1)$, matching the requirement and manifest. The input array itself is mutated, but input storage is not auxiliary space.

## Alternatives and edge cases

- **Hash set:** Insert every positive value, then test `1, 2, 3, ...`. This is simple and linear-time on average, but it uses $O(n)$ extra space and misses the constant-space requirement.
- **Boolean presence array:** Mark indices for values in $[1,n]$ and scan for the first unmarked entry. It makes the home-index idea explicit but still allocates $O(n)$ auxiliary memory.
- **Sign marking:** After normalizing unusable values, use the sign at index `v - 1` to mark value `v` present. This also achieves $O(n)$ time and $O(1)$ space, but requires care with repeated values and absolute values.
- **Sorting normally:** Sorting followed by a scan is straightforward and can be in place, but comparison sorting costs $O(n \log n)$ time.
- **Value `1` missing:** Index 0 will not contain `1` after placement, so the second pass immediately returns 1, regardless of large or negative values elsewhere.
- **All values `1` through `n` present:** Every home is correct and the algorithm returns `n + 1`.
- **Duplicates:** Once one copy occupies its home, the guard leaves additional copies alone. They neither cause an infinite loop nor generate false presence information.
- **Negative, zero, and oversized values:** The range condition ignores them safely. They do not need to be deleted or replaced.
- **A value already in place:** If `nums[i] == i + 1`, its computed destination is the same index and the equality guard prevents a pointless self-swap.
- **Input mutation:** The final order generally differs from the original. This is the tradeoff that supplies constant auxiliary space; callers needing the original order must pass a copy, which would itself use $O(n)$ space.
