# Find a Value of a Mysterious Function Closest to Target

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1521 |
| Difficulty | Hard |
| Topics | Array, Binary Search, Bit Manipulation, Segment Tree |
| Official Link | [find-a-value-of-a-mysterious-function-closest-to-target](https://leetcode.com/problems/find-a-value-of-a-mysterious-function-closest-to-target/) |

## Problem Description & Examples
### Goal
For every non-empty subarray, compute the bitwise AND of its elements. Return
the smallest absolute difference between any such value and `target`.

### Function Contract
**Inputs**

- `arr`: an integer array.
- `target`: the value to approach.

**Return value**

The minimum `abs(subarray_and - target)` over all non-empty subarrays.

### Examples
**Example 1**

- Input: `arr = [9, 12, 3, 7, 15], target = 5`
- Output: `2`

**Example 2**

- Input: `arr = [1000000, 1000000, 1000000], target = 1`
- Output: `999999`

**Example 3**

- Input: `arr = [1, 2, 4, 8, 16], target = 0`
- Output: `0`

---

## Underlying Base Algorithm(s)
Maintain the set of distinct bitwise AND values for subarrays ending at the
current index. To extend by `x`, the new set is `{x}` plus `prev & x` for every
previous ending value. The set stays small because bitwise AND can only turn bits
off, so update the best absolute difference at each step.

---

## Complexity Analysis
- **Time Complexity**: `O(n * b)`, where `b` is the number of bits in the values.
- **Space Complexity**: `O(b)`.
