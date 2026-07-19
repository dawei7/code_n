# Make Two Arrays Equal by Reversing Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1460 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/) |

## Problem Description
### Goal

You are given two integer arrays of equal length: `target`, which describes
the desired final order, and `arr`, which may be transformed. In one
operation, choose any non-empty contiguous subarray of `arr` and reverse the
order of all elements in that segment. You may perform the operation any number
of times, including zero.

Determine whether some sequence of allowed reversals can make `arr` exactly
equal to `target`. Reversals can change positions but never create, remove,
or alter values, so repeated values and their multiplicities must be handled
precisely.

### Function Contract
**Inputs**

- `target`: an integer array of length $n$.
- `arr`: another integer array of the same length $n$.
- $1 \le n \le 1000$, and every value in both arrays lies in $[1,1000]$.

**Return value**

Return `true` if repeated reversals of non-empty subarrays can transform
`arr` into `target`; otherwise return `false`.

### Examples
**Example 1**

- Input: `target = [1,2,3,4], arr = [2,4,1,3]`
- Output: `true`
- Explanation: Suitable reversals can reorder `arr` into the target order.

**Example 2**

- Input: `target = [7], arr = [7]`
- Output: `true`
- Explanation: No operation is necessary.

**Example 3**

- Input: `target = [3,7,9], arr = [3,7,11]`
- Output: `false`
- Explanation: Reversal cannot replace the value 11 with the missing value 9.
