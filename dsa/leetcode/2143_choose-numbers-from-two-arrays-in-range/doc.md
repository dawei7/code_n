# Choose Numbers From Two Arrays in Range

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2143 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [choose-numbers-from-two-arrays-in-range](https://leetcode.com/problems/choose-numbers-from-two-arrays-in-range/) |

## Problem Description

### Goal

Two 0-indexed integer arrays, `nums1` and `nums2`, have the same length $n$.
For an inclusive range $[l,r]$, choose exactly one value at every index: either
`nums1[i]` or `nums2[i]`.

The range and its choices are balanced when the sum of values chosen from
`nums1` equals the sum chosen from `nums2`. If no value is chosen from one
array, its sum is zero. Two balanced selections are different when either
endpoint differs or at least one index chooses the other array, even when the
two values at that index are equal.

Return the number of different balanced range selections modulo $10^9+7$.

### Function Contract

**Inputs**

- `nums1`: The first integer array.
- `nums2`: The second integer array, with the same length as `nums1`.

Their shared length satisfies $1 \leq n \leq 100$, and every value is between
$0$ and $100$, inclusive.

**Return value**

Return the number of endpoint-and-choice combinations whose two selected sums
are equal, reduced modulo $10^9+7$.

### Examples

**Example 1**

- Input: `nums1 = [1,2,5], nums2 = [2,6,3]`
- Output: `3`
- Explanation: One balanced selection uses range `[0,1]`; two distinct choice
  patterns balance range `[0,2]`.

**Example 2**

- Input: `nums1 = [0,1], nums2 = [1,0]`
- Output: `4`
- Explanation: Both singleton ranges have one zero-valued balanced choice, and
  the full range has two balanced choice patterns.
