# Apply Operations to an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2460 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Two Pointers, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/apply-operations-to-an-array/) |

## Problem Description

### Goal

You are given a 0-indexed array `nums` containing $n$ non-negative integers. Process each adjacent position from left to right, using indices $i=0,1,\ldots,n-2$. If `nums[i]` equals `nums[i + 1]`, replace `nums[i]` with twice its value and replace `nums[i + 1]` with `0`. Otherwise, leave both values unchanged. Because the operations are sequential, an earlier operation can change what a later index observes.

After all $n-1$ adjacent checks have been performed, move every zero to the end of the array while preserving the relative order of all nonzero values. Return the resulting array.

### Function Contract

**Inputs**

- `nums`: A list of $n$ non-negative integers.

The constraints are $2\le n\le2000$ and $0\le\texttt{nums[i]}\le1000$.

**Return value**

- The length-$n$ array after the sequential merge operations and stable zero shift.

### Examples

#### Example 1

- **Input:** `nums = [1, 2, 2, 1, 1, 0]`
- **Output:** `[1, 4, 2, 0, 0, 0]`
- **Explanation:** The equal `2` values become `4, 0`, then the equal `1` values become `2, 0`. Stable compaction leaves `1, 4, 2` before the zeros.

#### Example 2

- **Input:** `nums = [0, 1]`
- **Output:** `[1, 0]`
- **Explanation:** The adjacent values are unequal, so only the final zero shift changes the array.
